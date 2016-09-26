from django.shortcuts import render
from .genres_playlist import create_genres_from_dictionary
from string import ascii_uppercase

def index(request):
    genres = create_genres_from_dictionary()
    list_of_letters = list(ascii_uppercase)
    
    return render(request, 'genres/index.html', {'genres': genres, 'letters': list_of_letters})