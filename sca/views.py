from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import member_acc
from .models import currency




def all_members(request):
    mymembers = member_acc.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))

    
def currencypage(request):
    mymembers = currency.objects.all().values()
    template = loader.get_template("currency.html")
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))



def calculator(request):
    template = loader.get_template("calculator.html")
    return HttpResponse(template.render())


def homepage(request):
    template = loader.get_template("homepage.html")
    return HttpResponse(template.render())


def details(request, id):
  mymember = member_acc.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))