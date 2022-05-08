from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.organizationHome, name="organizationHome"),
    path('job/', views.organizationJob, name="organizationJob"),
    path('orgProfile/', views.organizationProfile, name="organizationProfile"),
    path('editOrgProfile/', views.organizationEditProfile, name="organizationEditProfile"),
    path('editJob/<job_id>/', views.editJob, name="editJob"),
    path('deleteJob/<job_id>/', views.deleteJob, name="deleteJob"),
    path('viewJob/<job_id>/', views.viewJob, name="viewJob")
]