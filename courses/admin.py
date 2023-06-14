from django.contrib import admin
from .models import Course, Category, Comment
from django.utils.text import slugify
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)


admin.site.register(Course, CourseAdmin)
admin.site.register(Category)
admin.site.register(Comment)
