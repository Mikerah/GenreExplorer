from django.shortcuts import render
from .genres_playlist import create_genres_from_dictionary
from .constants import LIST_OF_LETTERS

def index(request):
    genres = create_genres_from_dictionary()
    return render(request, 'genres/index.html', {'genres': genres, 'letters': list_of_letters})