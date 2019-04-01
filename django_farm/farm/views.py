from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

# from .models import Game, Mode, State

import json

def home_view(request):

    return render(request, "farm/farm_sim.html", {})


def save_state(request):
    
    data = json.loads(request.body)
    
        energy = data['energy']
        filth = data['filth']
        day_light = data['day_light']
        milk = data['milk']
        milk_val = data['milk_val']
        eggs = data['eggs']
        eggs_val = data['eggs_val']
        bacon = data['bacon']
        bacon_val = data['bacon_val']
        money = data['money']
        wallet = data['wallet']
        cow_price = data['cow_price']
        cow_count = data['cow_count']
        pig_price = data['pig_price']
        pig_count = data['pig_count']
        coop_price = data['coop_price']
        coop_count = data['coop_count']
                
    player = request.user
    state = State(energy=energy, filth=filth, day_light=day_light, milk=milk, milk_val=milk_val, eggs=eggs, eggs_val=eggs_val, bacon=bacon, bacon_val=bacon_val, money=money, wallet=wallet, cow_price=cow_price, cow_count=cow_count, pig_price=pig_price, pig_count=pig_count, coop_price=coop_price, coop_count=coop_count)
    state.save()
    return HttpResponse('hi')
