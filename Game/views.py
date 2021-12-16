from django.shortcuts import render

from Game.models import Place
from Game.models import Enemy
from Game.models import Weapon
from Game.models import Boss
# Create your views here.

x,y = 0,0
enemy='пока что тут никого нету'

def greet(request):
    return render(request, 'Game/greetings.html')

def travel(request):
    global y
    global x
    global enemy
    last=[x, y]
    if request.method == 'POST':
        if request.POST['direction'] == 'w' and Place.objects.filter(x=x,y=y+1):
            y+=1
        elif request.POST['direction']=='s'and Place.objects.filter(x=x,y=y-1):
            y-=1
        elif request.POST['direction']=='a'and Place.objects.filter(x=x-1,y=y):
            x-=1
        elif request.POST['direction']=='d' and Place.objects.filter(x=x+1,y=y):
            x+=1

    current_place=Place.objects.get(x=x, y=y)
    if last!=[x,y] or current_place.name=='Замок':
        msg=current_place.msg
    else:
        msg='Вы не можете пройти дальше'
    
    if current_place.enemy == 1:
        enemy = Enemy.objects.get(x=x, y=y)  
    elif current_place.enemy == 2:
        enemy = Boss.objects.get(x=x, y=y) 
    else:
        enemy='пока что тут никого нету'

    context={'x':x, 'y':y, 'msg':msg, 'place':current_place,'enemy':enemy}
    return render(request, 'Game/travel.html', context)

def fight(request):
    global y
    global x


    current_place=Place.objects.get(x=x, y=y)
    
    if current_place.enemy==2:
         current_enemy=Boss.objects.get(x=x, y=y)
    else:
        current_enemy=Enemy.objects.get(x=x, y=y)

    enemy = current_enemy.name
    hp=current_enemy.hp
    damage=current_enemy.damage

    context={'hp':hp, 'damage':damage,'enemy':enemy}
    return render(request, 'Game/fight.html',context)