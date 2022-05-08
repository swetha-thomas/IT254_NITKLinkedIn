from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.organizationHome, name="organizationHome"),
    path('job/', views.organizationJob, name="organizationJob"),
    path('orgProfile/', views.organizationProfile, name="organizationProfile"),
    path('editOrgProfile/', views.organizationEditProfile, name="organizationEditProfile"),
    path('editJob/', views.editJob, name="editJob"),
    path('deleteJob/', views.deleteJob, name="deleteJob"),
    path('viewJob/', views.viewJob, name="viewJob")
]
