
from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.courses, name='courses'),
    path('<str:slug>', views.course_desc, name='course_desc'),
    path('courses/list', views.courses_list, name='courses_list'),
]
