from django.contrib import admin

from Game.models import Boss, Place
from Game.models import Enemy
from Game.models import Weapon
# Register your models here.
admin.site.register(Place)
admin.site.register(Enemy)
admin.site.register(Weapon)
admin.site.register(Boss)