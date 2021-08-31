from django.contrib import admin
from django.urls import path, include
from loggingfile import views

urlpatterns = [
            path('log1/', views.find_sum),
            path('log2/', views.makelogs)
               ]
