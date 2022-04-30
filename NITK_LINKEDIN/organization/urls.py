from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.organizationHome, name="organizationHome"),
    path('jobs/', views.organizationJobs, name="organizationJobs"),
    path('orgProfile/', views.organizationProfile, name="organizationProfile"),
    path('editOrgProfile/', views.organizationEditProfile, name="organizationEditProfile")
]
