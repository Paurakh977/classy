from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path("",views.task,name='tasks'),
    path("uploadnotes",views.upload_notes,name="upload_notes"),
    path("viewnotes",views.view_notes,name="view_notes"),
]
