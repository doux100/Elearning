
from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.courses, name='courses'),
    path('list', views.courses_list, name='courses_list'),
    path('<str:slug>', views.course_desc, name='course_desc'),
    path('<str:slug>/enroll', views.courses_enroll, name='courses_enroll'),
    path('courses/enrolled', views.enroll_done, name='enroll_done'),
]
