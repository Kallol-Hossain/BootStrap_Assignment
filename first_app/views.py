from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_app2(request):
    return render(request, 'first_app/first_app.html' , {"shakib": 65, 'Tamim':70})
