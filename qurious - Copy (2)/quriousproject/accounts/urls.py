from django.urls import path
from .views import*


urlpatterns = [
   
    path('',home_view,name='accounts_home'),
    path('login/',login_view,name='accounts_login'),
    path('signup/',signup_view,name='accounts_signup'),
    path('logout/',login_out,name='accounts_logout'),
    
    
]