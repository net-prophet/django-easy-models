from django.db import models

from EasyModels import FullNameModel, StrongPKModel

class Customer(FullNameModel, StrongPKModel):
    state = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=1, blank=True)
    age = models.IntegerField(blank=True)