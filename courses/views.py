from django.shortcuts import render
from .models import Course, Category
# Create your views here.


def courses(request):
    course = Course.objects.all()
    category = list(Category.objects.all())
    for c in category:
        c.coursecount = len(course.filter(category=c))
        print(c.coursecount)
    cont = {'course': course, 'category': category}
    return render(request, 'courses.html', cont)
