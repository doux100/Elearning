import random
from django.shortcuts import render
from courses.models import Category, Course, Comment
from our_team.models import Team


# Create your views here.
def home(request):
    course = Course.objects.order_by('?')
    category = list(Category.objects.all())
    for c in category:
        c.coursecount = len(course.filter(category=c))
    team = Team.objects.all()[:4]
    student = Comment.objects.order_by('?')[:4]
    cont = {'course': course, 'category': category,
            'team': team, 'student': student}
    return render(request, 'index.html', cont)
