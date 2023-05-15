from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from django.http import JsonResponse
from django.db.models import Q

from .models import Friend, Friend_request
from .serializers import *
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Friends(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        friends = FriendSerializer(Friend.objects.filter(first_user_id=request.user.id), many=True)
        return Response(friends.data)

class FriendSender(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        applications = FriendSenderSerializer(Friend_request.objects.filter(sender_id=request.user.id), many=True)
        return Response(applications.data)

class FriendRecipient(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        applications = FriendRecipientSerializer(Friend_request.objects.filter(recipient_id=request.user.id), many=True)
        return Response(applications.data)


def add_friends(first_user, second_user):
    Friend.objects.create(first_user_id=first_user, second_user_id=second_user)
    Friend.objects.create(first_user_id=second_user, second_user_id=first_user)

def friend_request_action(request, only_delete=False):
    user_type = request.query_params.get('type')
    if user_type == 'id':
        id_user = request.query_params.get('id')        
    elif user_type == 'name':
        id_user = User.objects.filter(username=request.query_params.get('name'))
        if len(id_user) == 0:
            content = {'erorr': 'Not found name.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:  
            id_user = id_user[0].id
    else:
        content = {'erorr': 'Not found type.'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    f_request = Friend_request.objects.filter(Q(sender_id=id_user) | Q(recipient_id=request.user.id))
    if len(f_request) == 0:
        content = {'erorr': 'Not found name.'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    else:
        f_request = f_request[0]
        if not only_delete:
            add_friends(id_user, request.user.id)
        f_request.delete()
        return Response({}, status=status.HTTP_202_ACCEPTED)  

    return Response({'erorr': ''}, status=status.HTTP_400_BAD_REQUEST) 


class FriendAcceptRequest(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        return friend_request_action(request)
        
class FriendCancelRequest(FriendAcceptRequest):
    def get(self, request, format=None):
        return friend_request_action(request, True)


class FriendSendRequest(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user_type = request.query_params.get('type')
        if user_type == 'id':
            id_user = request.query_params.get('id')        
        elif user_type == 'name':
            id_user = User.objects.filter(username=request.query_params.get('name'))
            if len(id_user) == 0:
                content = {'erorr': 'Not found name.'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            else:  
                id_user = id_user[0].id
        else:
            content = {'erorr': 'Not found type.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        f_request = Friend_request.objects.filter(Q(sender_id=id_user) | Q(recipient_id=request.user.id))
        if len(f_request) == 0:
            Friend_request.objects.create(sender_id=request.user.id, recipient_id=id_user)
        else:
            add_friends(id_user, request.user.id)
            f_request.delete()

        return Response({}, status=status.HTTP_202_ACCEPTED)  
    

class FriendDelete(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user_type = request.query_params.get('type')
        if user_type == 'id':
            id_user = request.query_params.get('id')        
        elif user_type == 'name':
            id_user = User.objects.filter(username=request.query_params.get('name'))
            if len(id_user) == 0:
                content = {'erorr': 'Not found name.'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            else:  
                id_user = id_user[0].id
        else:
            content = {'erorr': 'Not found type.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        node1 = Friend.objects.filter(first_user_id=id_user, second_user_id=request.user.id)
        node2 = Friend.objects.filter(first_user_id=request.user.id, second_user_id=id_user)
        if len(node1) != 0:
            node1[0].delete()
            node2[0].delete()
            return Response({}, status=status.HTTP_200_OK) 

        content = {'erorr': 'The user is not your friend.'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

class FriendStatus(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user_type = request.query_params.get('type')
        if user_type == 'id':
            id_user = request.query_params.get('id')        
        elif user_type == 'name':
            id_user = User.objects.filter(username=request.query_params.get('name'))
            if len(id_user) == 0:
                content = {'erorr': 'Not found name.'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            else:  
                id_user = id_user[0].id
        else:
            content = {'erorr': 'Not found type.'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        f_request = Friend_request.objects.filter(sender_id=id_user, recipient_id=request.user.id)
        if len(f_request) != 0:
            return Response({"status": "incoming_request", "description": "There is an incoming request."}, status=status.HTTP_200_OK) 

        f_request = Friend_request.objects.filter(sender_id=request.user.id, recipient_id=id_user)
        if len(f_request) != 0:
            return Response({"status": "outgoing_request", "description": "There is an outgoing request."}, status=status.HTTP_200_OK)

        f_request = Friend.objects.filter(first_user_id=request.user.id, second_user_id=id_user)
        if len(f_request) != 0:
            return Response({"status": "friend", "description": "Already friends."}, status=status.HTTP_200_OK)

        return Response({"status": "none", "description": "There is nothing."}, status=status.HTTP_200_OK)





    """
    def get(self, request, format=None):
        class UserDetail(generics.RetrieveAPIView):
    
        #return Response(serializer.data)

    def post(self, request, format=None):
       # serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """

"""
class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response()#serializer.data)

    def post(self, request, format=None):
       # serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""