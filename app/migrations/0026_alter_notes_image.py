# Generated by Django 4.2.5 on 2023-10-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_notes_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/image/user_media'),
        ),
    ]
