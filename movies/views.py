from urllib import request
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    template = "movies/index.html"
    return render(request, template, {"movies": movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    template = "movies/detail.html"
    return render(request, template, {"movie": movie})
