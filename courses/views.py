from .filters import CourseFilter
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Course, Category, Comment
from .forms import CommentForm
# Create your views here.


def courses(request):
    course = Course.objects.all()
    category = list(Category.objects.all())
    student = Comment.objects.order_by('?')
    for c in category:
        c.coursecount = len(course.filter(category=c))
        print(c.coursecount)
    cont = {'course': course, 'category': category, 'student': student}
    return render(request, 'courses.html', cont)


@login_required
def course_desc(request, slug):
    course = Course.objects.get(slug=slug)
    # comments
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data['comment']
            Comment.objects.create(
                user=request.user, course=course, comment=comment_text)
            return redirect(request.path)
    else:
        form = CommentForm()
    cont = {'form': form, 'course': course}
    return render(request, 'desc.html', cont)


def courses_list(request):
    courses = Course.objects.all()
    filter = CourseFilter(request.GET, queryset=courses)
    cont = {
        'courses': filter.qs,
        'form': filter.form,
    }
    return render(request, 'courses_list.html', cont)
