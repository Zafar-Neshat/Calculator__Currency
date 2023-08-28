from django.db import models

class member_acc(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  Date = models.DateField(null=True)