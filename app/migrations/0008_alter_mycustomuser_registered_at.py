# Generated by Django 4.2.2 on 2023-07-31 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_mycustomuser_registered_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycustomuser',
            name='registered_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
