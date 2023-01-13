from django.http import HttpResponse
from django.shortcuts import render
from .models import place, food


# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=food.objects.all()
    return render(request,'index.html',{"result":obj,"results":obj1})