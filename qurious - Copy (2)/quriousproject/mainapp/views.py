from django.shortcuts import render,redirect

# Create your views here.



 
def members_list(request):

       
    return render(request,template_name='mainapp/members_list.html')
    

def edit(request,id):
    return render(request,'mainapp/update.html')

def add_member(request):
    return render(request,'mainapp/addmember.html')

    # -------------------

def dashboard(request):
    return render(request,'mainapp/dashboard.html')


def deals(request):
    return render(request,'mainapp/deals.html')

def settings(request):
    return render(request,'mainapp/settings.html')
def service(request):
    return render(request,'userapp/service.html')

def enquiry(request):
    return render(request,'mainapp/enquiry.html')

def booking(request):
    return render(request,'mainapp/booking.html')