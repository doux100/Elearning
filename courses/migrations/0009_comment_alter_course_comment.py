# Generated by Django 4.2.1 on 2023-06-13 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='comment',
            field=models.ManyToManyField(related_name='user_comment', to='courses.comment'),
        ),
    ]