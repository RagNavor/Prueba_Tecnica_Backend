from django.urls import path
from .views import DataResume


urlpatterns = [
    path('resume/',DataResume.as_view(),name='resume' )
    #path('post',Login.as_view(),name='login'),
    #path('logout',Logout.as_view(), name='logout')
    
]