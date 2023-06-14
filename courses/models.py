from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="category/")

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.TextField(max_length=250)


class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    period = models.DecimalField(max_digits=5, decimal_places=2)
    instructor = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='courses/')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='comments', null=True)
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.course.name}"
