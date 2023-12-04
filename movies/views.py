from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    template = "movies/index.html"
    return render(request, template, {"movies": movies})
