from django.urls import path
from .views import*


urlpatterns = [
   
    path('members/',members_list,name='mainapp_members_list'),
    path('edit/<int:id>',edit,name='mainapp_edit'),
    path('addmember/',add_member,name='mainapp_addmember'),

    # -------
    path('dashboard/',dashboard,name='mainapp_dashboard'),
    path('booking/',booking,name='mainapp_booking'),
    path('deals/',deals,name='mainapp_deals'),
    path('enquiry/',enquiry,name='mainapp_enquiry'),
    path('settings/',settings,name='mainapp_settings'),
    path('service/',service,name='mainapp_service'),
]