from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

# from .models import Game, Mode, State

import json

def home_view(request):

    return render(request, "farm/farm_sim.html", {})
