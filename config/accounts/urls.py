from django.urls import path 
from accounts.views import UserRegisterView,UserRegisterVerifyCode, UserLoginView,UserLogOutView
app_name = 'accounts' 

urlpatterns = [
  path('register/', UserRegisterView.as_view(), name='user_register'),
  path('verify/', UserRegisterVerifyCode.as_view(), name='verify_code'),
  path('login/', UserLoginView.as_view(), name='user_login'),
  path('logout/', UserLogOutView.as_view(), name='user_logout'),
]
