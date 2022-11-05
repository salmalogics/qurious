from django.shortcuts import render

# Create your views here.
def users_view(request):
    return render(request,'userapp/userhome.html')

def profile(request):
    return render(request,'userapp/profile.html')
def service(request):
    return render(request,'userapp/service.html')