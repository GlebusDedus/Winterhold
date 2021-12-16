from django.db import models

# Create your models here.
class Place(models.Model):
    x=models.IntegerField(blank=False, default=0)
    y=models.IntegerField(blank=False, default=0)
    name=models.CharField(max_length=20)
    msg=models.TextField()
    enemy=models.IntegerField(blank=False, default=0,null=True)

    def __str__(self) -> str:
        return self.name

class Enemy(models.Model):
    x=models.IntegerField(blank=False, default=0)
    y=models.IntegerField(blank=False, default=0)
    name=models.CharField(max_length=21)
    damage=models.IntegerField(blank=False, default=0)
    hp=models.IntegerField(blank=False, default=0,null=True)

    def __str__(self) -> str:
        return self.name

class Weapon(models.Model):
    name=models.CharField(max_length=21)
    damage=models.IntegerField(blank=False, default=0)
    cost=models.IntegerField(blank=False, default=0)
    classification=models.CharField(max_length=21)
    block_chance=models.FloatField(blank=False, default=0,null=True)
    dodge_chance=models.FloatField(blank=False, default=0,null=True)
    second_chancee=models.IntegerField(blank=False, default=0,null=True)
    ad_dod_chancee=models.IntegerField(blank=False, default=0,null=True)
    ad_damagee=models.IntegerField(blank=False, default=0,null=True)
    first_hite=models.IntegerField(blank=False, default=0,null=True)
    near_fight_dmge=models.FloatField(blank=False, default=0,null=True)
    crit_chance=models.IntegerField(blank=False, default=20,null=True)


    def __str__(self) -> str:
        return self.name

class Boss(models.Model):
    x=models.IntegerField(blank=False, default=0)
    y=models.IntegerField(blank=False, default=0)
    name=models.CharField(max_length=21)
    damage=models.IntegerField(blank=False, default=0)
    hp=models.IntegerField(blank=False, default=0,null=True)
    drop=models.CharField(max_length=21)

    def __str__(self) -> str:
        return self.name