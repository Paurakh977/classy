# Generated by Django 4.2.5 on 2023-10-20 04:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_notes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='chapter_no',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=32, message='Chapter number must be between 1 and 32')]),
        ),
        migrations.AlterField(
            model_name='notes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
