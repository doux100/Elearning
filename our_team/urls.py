
from django.urls import path
from . import views

app_name = 'our_team'
urlpatterns = [
    path('', views.our_team, name='our_team'),
]
