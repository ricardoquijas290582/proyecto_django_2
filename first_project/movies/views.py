from django.shortcuts import render
from django.http import HttpResponse
from django import views
from .models import Movie

# Create your views here.

def GetMovies(request):
    # Vamos a traer todos las películas
    movies = Movie.objects.all() # SELECT * FROM movies_movie #queryset
    print(movies)
    return HttpResponse('Sí funciona mi estimado, vamos bien!')
    #template_name = 'movies/list.html'
    #context = {
    #    'movies': movies
    #}
    #return render(request, template_name, context)