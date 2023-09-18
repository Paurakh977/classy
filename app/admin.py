from django.contrib import admin
from app.models import MyCustomUser,Contacts,Todo
admin.site.register(MyCustomUser)
admin.site.register(Contacts)
admin.site.register(Todo)