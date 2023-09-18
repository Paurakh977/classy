from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone

USERNAME_REGEX = r'^[\w\s.@+-]+$'

username_validator = RegexValidator(
    regex=USERNAME_REGEX,
    message='Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.',
)

class MyCustomUser(AbstractUser):
    roll = models.CharField(max_length=5,unique=True)
    bio = models.CharField(max_length=150, default='Adventurous explorer of knowledge, always eager to learn and grow. 📚🚀')
    username = models.CharField(max_length=150,unique=True,validators=[username_validator],
    error_messages={'unique': "A user with that username or roll already exists.",},)
    registered_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}  ({self.roll})"

class Contacts(models.Model):
    user=models.ForeignKey(MyCustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=17)
    email=models.EmailField()
    desc=models.TextField()

    def __str__(self):
        return f"{self.email} ({self.user}) "
    
class Todo(models.Model):
    user=models.ForeignKey(MyCustomUser,on_delete=models.CASCADE)    
    task=models.CharField(max_length=30)
    desc=models.TextField()
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.task} {self.user}"