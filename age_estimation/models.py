from django.contrib.auth.models import User
from django.db import models


class UserInfo(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    frequency = models.FloatField()
    frequency2 = models.FloatField(default=100)
    average = models.FloatField(default=100)
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    def __unicode__(self):
        return str(self.id)


class Learn(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    caption = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return str(self.id)
