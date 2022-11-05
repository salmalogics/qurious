from django.urls import path
from .views import*


urlpatterns = [
   path('',users_view,name='userapp_userpage'),
   path('profile/',profile,name='userapp_profile'),
   path('service/',service,name='userapp_services'),

   
]