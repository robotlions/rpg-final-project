from django.db import models
from django.conf import settings

class Weapon(models.Model):
    pass


# Create your models here.
class Character(models.Model):

    WARRIOR = 'Warrior'
    MAGICIAN = 'Magician'
    JOB_CHOICES = [
        (WARRIOR, 'Warrior'),
        (MAGICIAN, 'Magician'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    level = models.IntegerField(null=True)
    hp = models.IntegerField(null=True)
    ac = models.IntegerField(null=True)
    hpmax = models.IntegerField(null=True)
    sp = models.IntegerField(null=True)
    spmax = models.IntegerField(null=True)
    xp = models.IntegerField(null=True)
    job = models.CharField(
        max_length=15,
        choices=JOB_CHOICES,
        default=WARRIOR, null=True)

    def __str__(self):
        return self.name
