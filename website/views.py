from django.shortcuts import render,redirect

from django.utils.decorators import method_decorator

from django.views.generic import ListView 
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
import requests 

# Create your views here.


class loginpage(ListView):
    def get (self,request):
        return render (request,'outsite/loginpage.html')
    def post (self,request):

        username = request.POST['Username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
           auth.login(request,user)
           return redirect('index')
        else :
            print("NODATA")
            return redirect('/')
        


class index(ListView):
    def get (self,request):
        datafromiot = requests.get('http://45.136.236.39:8005/get_all_fromIot/').json()['detail'] 
        lastesdata7 = datafromiot[-7:]
        context = {
            'lastesdata7':lastesdata7
        }
        return render(request, 'insite/index.html',context)



