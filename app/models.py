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

import os
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator
from django.utils import timezone

def get_upload_path(instance, filename):
    return  f'static/image/media/{instance.subject}/{filename}'

class Notes(models.Model):
    subject = models.CharField(max_length=15, default="")
    document = models.FileField(upload_to=get_upload_path, default='')
    user = models.ForeignKey(MyCustomUser, on_delete=models.CASCADE)
    chapter_no = models.PositiveIntegerField(
        validators=[MaxValueValidator(limit_value=32, message="Chapter number must be between 1 and 32")]
    )
    page = models.CharField(max_length=15)
    title = models.CharField(max_length=40)
    desc = models.TextField()
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.title} by {self.user} subject: {self.subject} "

    def delete(self, using=None, keep_parents=False):
        # Delete the document if it exists
        if self.document:
            document_path = os.path.join(settings.MEDIA_ROOT, str(self.document))
            if os.path.exists(document_path):
                os.remove(document_path)

        super(Notes, self).delete(using=using, keep_parents=keep_parents)

    def save(self, *args, **kwargs):
        # Check if the instance already exists in the database
        if self.pk is not None:
            # Get the old instance
            old_instance = Notes.objects.get(pk=self.pk)

            # If the title is changed, delete the old document
            if self.title != old_instance.title and old_instance.document:
                old_document_path = os.path.join(settings.MEDIA_ROOT, str(old_instance.document))
                if os.path.exists(old_document_path):
                    os.remove(old_document_path)

        super(Notes, self).save(*args, **kwargs)

class profilepics(models.Model):
    img=models.ImageField(upload_to="static/image/media/profiles/")
    user=models.ForeignKey(MyCustomUser, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(default=timezone.now())
    def __str__(self) -> str:
        return f"{self.user} img: {self.img}"