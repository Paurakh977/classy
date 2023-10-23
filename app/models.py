from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.db import models
import os
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
    roll=models.CharField(max_length=4,default="")
    email=models.EmailField()
    desc=models.TextField()
    time=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.email} from {self.user} at {self.time.strftime('%Y-%m-%d')} "
    
class Todo(models.Model):
    user=models.ForeignKey(MyCustomUser,on_delete=models.CASCADE)    
    task=models.CharField(max_length=30)
    desc=models.TextField()
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.task} {self.user}"

class Notes(models.Model):
    document=models.FileField(upload_to="static/image/user_media",default='')
    subject=models.CharField(max_length=15,default="")
    user=models.ForeignKey(MyCustomUser,on_delete=models.CASCADE)
    chapter_no = models.PositiveIntegerField(
        validators=[MaxValueValidator(limit_value=32, message="Chapter number must be between 1 and 32")])
    page=models.PositiveIntegerField()
    title=models.CharField(max_length=40)
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return f"{self.title} by {self.user} subject:{self.subject} "
    
    def delete(self, *args, **kwargs):
        # Before deleting the object, delete the associated image file.
        if self.image:
            image_path = os.path.join(settings.MEDIA_ROOT, str(self.image))
            if os.path.exists(image_path):
                os.remove(image_path)
        super(Notes, self).delete(*args, **kwargs)
