from django.contrib import admin
from django.urls import path,include
from app import views


from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.task,name='tasks'),
    path("uploadnotes/<str:sub>", views.upload_notes, name="upload_notes"),
    path("viewnotes/<str:sub>",views.view_notes,name="view_notes"),
    path('full_view_notes/<str:chapter>/<str:title>/', views.full_view, name='full_view'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
