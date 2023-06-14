# Generated by Django 4.2.1 on 2023-06-13 17:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0007_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='comment',
            field=models.ManyToManyField(related_name='user_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]