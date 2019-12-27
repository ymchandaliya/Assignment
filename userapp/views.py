# from django.http import HttpResponse
from django.shortcuts import render
# from django.views import generic
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
from .models import UserProfile
# Create your views here.

def index(request):
    return render(request,template_name='index.html')

def SignUpView(request):

    if request.method == 'POST':

        user = UserProfile.objects.create_user(email=request.POST['email'],FirstName=request.POST['fname'],LastName=request.POST['lname'],Role=request.POST['radioBtn'],mobile=request.POST['mobile'],password=request.POST['password'])
        # print(request.POST['password'])

        # user.save()

        return render(request,template_name='index.html')
