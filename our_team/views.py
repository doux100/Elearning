from django.shortcuts import render
from .models import Team
# Create your views here.


def our_team(request):
    team = Team.objects.all()
    cont = {'team': team}
    return render(request, 'team.html', cont)
