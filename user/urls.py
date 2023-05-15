from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('api-token/', obtain_auth_token),
    path('friend/', views.Friends.as_view()),
    path('friend-request/sender/', views.FriendSender.as_view()),
    path('friend-request/receive/', views.FriendRecipient.as_view()),
    path('friend-request/accept/', views.FriendAcceptRequest.as_view()),
    path('friend-request/cancel/', views.FriendCancelRequest.as_view()),
    path('friend-request/send/', views.FriendSendRequest.as_view()),
    path('friend/delete/', views.FriendDelete.as_view()),
    path('friend/status/', views.FriendStatus.as_view()),
    
    
    
    
    
    
    #path('login/', views.ExampleView.as_view()),
    
    #path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)