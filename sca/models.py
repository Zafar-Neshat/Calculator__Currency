from django.db import models

class member_acc(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  Date = models.DateField(null=True)

  def __str__(self):
    return "{self.firstname} {self.lastname}"



class currency(models.Model):
  Currencyone = models.CharField(max_length=255)
  Currencytwo = models.CharField(max_length=255)
  Valueone = models.CharField(max_length=255)
  Valuetwo = models.CharField(max_length=255)
  
  def __str__(self):
    return "{self.Currencyone} {self.Currencytwo} {self.Valueone} {self.Valuetwo}"