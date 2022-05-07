from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentHome, name="studentHome"),
    path('job/', views.studentJob, name="studentJob"),
    path('profile/', views.studentProfile, name="studentProfile"),
    path('editProfile/', views.studentEditProfile, name="studentEditProfile"),
    path('addWorkExp/', views.studentAddExp, name="studentAddExp"),
    path('addClub/', views.studentAddClub, name="studentAddClub"),
    path('addSkills/', views.studentAddSkills, name="studentAddSkills"),
    path('addEducation/', views.studentAddEducation, name="studentAddEducation"),
    path('addCourses/', views.studentAddCourses, name="studentAddCourses")




]
