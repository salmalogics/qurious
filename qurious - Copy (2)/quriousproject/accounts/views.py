from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from .forms import MemberForm
from .models import*
def home_view(request):
    return render(request,'accounts/home.html')


def login_view(request):
    if request.method =='GET':
        return render(request,'accounts/login.html')
    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        admin=authenticate(username=username,password=password)
        if admin is not None:
            login(request,admin)
            if admin.user_type=='admin':
                return redirect('mainapp')
            else:
                return redirect('userapp')
        return render(request,'accounts/login.html',{'error': "Invalid username/password !"})
        







        return render(request,'accounts/login.html')
        

def signup_view(request):
    if request.method=='GET':
        context={}
        context['form']=MemberForm()
        return render(request,'accounts/signup.html',context)
    elif request.method=='POST':
        form=MemberForm(request,'POST')
        if form.is_valid():
            form.save()
            return redirect('accounts_signup')




def login_out(request):
    logout(request)
    return redirect('accounts_home')