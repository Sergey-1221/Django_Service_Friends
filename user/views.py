from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from django.http import JsonResponse

from .models import Friend, Friend_request
from .serializers import *
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token




class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

# 94e943a26fcc653c9918063f98e2f236bf677567
"""
class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        #token = Token.objects.create(user=request.user)
        #print(token.key)
        return Response(content)
"""

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