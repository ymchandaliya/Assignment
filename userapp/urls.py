from django.urls import path
from .views import SignUpView,index
urlpatterns = [
    path('',index),
    path('success',SignUpView,name='SignUpView')
]
