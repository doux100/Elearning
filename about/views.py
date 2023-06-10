from django.shortcuts import render
from our_team.models import Team
# Create your views here.


def about(request):
    team = Team.objects.all()
    cont = {'team': team}
    return render(request, 'about.html', cont)
