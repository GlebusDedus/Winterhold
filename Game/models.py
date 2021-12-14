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