"""
URL configuration for Classy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup_page, name='signup'),
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout_page, name='logout'),
    path('contactus/',views.contact,name='contact'),
    path('aboutus/',views.about,name='about'),
    path('profile/',views.profile,name='profile'),
    path('tasks/',include("app.urls"),name='tasks'),
    path('routine/',views.routine,name='routine'),
    path('bio/<int:id>/',views.bio,name='bio'), 
    path('updatebio',views.bio_up,name='bioupdate'),
    path('todo',views.todo,name='todo'),
    path('add',views.add,name='add'),
    path('update_todo/<int:task_id>/',views.update_todo,name='update_todo'),
    path('delete_todo/<int:id>/',views.delete_todo,name='delete_todo'),
    path('get_copy_content/', views.get_copy_content, name='get_copy_content'),
    path('get_email_content/', views.get_email_content, name='get_email_content'),
    path('upload_profile/',views.upload_profile,name='upload_profile'),

]