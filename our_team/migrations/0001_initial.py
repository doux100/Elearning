# Generated by Django 4.2.1 on 2023-05-27 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='team/')),
                ('facebook', models.URLField(null=True)),
                ('twitter', models.URLField(null=True)),
                ('instagram', models.URLField(null=True)),
            ],
        ),
    ]