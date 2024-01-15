from django.urls import path
from .views import UserApi, Login, Logout


urlpatterns = [
    path('',UserApi.as_view(),name='users' ),
    path('login',Login.as_view(),name='login'),
    path('logout',Logout.as_view(), name='logout')
    
]
