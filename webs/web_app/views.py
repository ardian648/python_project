from django.shortcuts import render
from django.http import HttpResponse



def home(request):

    return render(request, "web_app/home.html", {'title': 'home'})


# context isn't working because we didn't start the database and make migration