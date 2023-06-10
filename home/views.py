from django.shortcuts import render
from courses.models import Category, Course
from our_team.models import Team


# Create your views here.
def home(request):
    course = Course.objects.all()
    category = list(Category.objects.all())
    for c in category:
        c.coursecount = len(course.filter(category=c))
        print(c.coursecount)
    team = Team.objects.all()
    cont = {'course': course, 'category': category, 'team': team}
    return render(request, 'index.html', cont)
