from django.db import models

class TitanicPassenger(models.Model):
    passenger_id = models.IntegerField(primary_key=True)
    survived = models.BooleanField()
    pclass = models.IntegerField()
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    age = models.FloatField(null=True, blank=True)
    sibsp = models.IntegerField()
    parch = models.IntegerField()
    ticket = models.CharField(max_length=20)
    fare = models.FloatField()
    cabin = models.CharField(max_length=20, null=True, blank=True)
    embarked = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name} ({self.passenger_id})'
