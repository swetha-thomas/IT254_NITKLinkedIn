from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentHome, name="studentHome"),
    path('job/', views.studentJob, name="studentJob"),
    path('profile/', views.studentProfile, name="studentProfile"),
    path('editProfile/', views.studentEditProfile, name="studentEditProfile"),
]
