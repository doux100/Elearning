from django.conf import settings
from django.core.mail import send_mail
from .filters import CourseFilter
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render,get_object_or_404
from .models import Course, Category, Comment
from .forms import CommentForm
# Create your views here.


def courses(request):
    course = Course.objects.all()
    category = list(Category.objects.all())
    student = Comment.objects.order_by('?')[:6]
    for c in category:
        c.coursecount = len(course.filter(category=c))
    cont = {'course': course, 'category': category, 'student': student}
    return render(request, 'courses.html', cont)


def courses_list(request):
    courses = Course.objects.all()
    filter = CourseFilter(request.GET, queryset=courses)
    cont = {
        'courses': filter.qs,
        'form': filter.form,
    }
    return render(request, 'courses_list.html', cont)


@login_required
def course_desc(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data['comment']
            Comment.objects.create(
                user=request.user, course=course, comment=comment_text)
            return redirect(request.path)
    else:
        form = CommentForm()

    student = Comment.objects.all().filter(course_id=course.pk)

    cont = {'form': form, 'course': course, 'student': student}
    return render(request, 'desc.html', cont)


@login_required
def courses_enroll(request, slug):
    course = Course.objects.get(slug=slug)
    if request.method == 'POST':
        name = request.user
        email = request.user.email
        subject = course
        send_mail(
            subject,
            f'\"{name}\" Want to enroll in {course} \nSender Email is : {email}',
            email,
            [settings.EMAIL_HOST_USER],
        )
        return redirect('courses:enroll_done')
    return render(request, 'enroll.html', {'course': course})


def enroll_done(request):
    return render(request, 'enroll_done.html')
