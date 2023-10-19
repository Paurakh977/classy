from django.contrib import admin
from app.models import MyCustomUser,Contacts,Todo,Notes
admin.site.register(MyCustomUser)
admin.site.register(Contacts)
admin.site.register(Todo)
admin.site.register(Notes)

