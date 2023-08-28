from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import member_acc



def all_members(request):
    mymembers = member_acc.objects.all().values()

    template = loader.get_template("all_members.html")

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

def currency(request):
    template = loader.get_template("currency.html")
    return HttpResponse(template.render())