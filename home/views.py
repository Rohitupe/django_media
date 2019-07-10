from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# Create your views here.
def home(request):
    obj = Employee.objects.all()
    context = {
        'objects':obj
    }
    return render(request,'home.html',context)
    
def detail(request):
    pass