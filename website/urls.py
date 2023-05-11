from django.contrib import admin
from django.urls import path,include

from .views import loginpage,index

urlpatterns = [
    # path('',include("django.contrib.auth.urls")),
    path('',loginpage.as_view(), name="loginpage"),
    path('index', index.as_view(), name="index"), 
]
