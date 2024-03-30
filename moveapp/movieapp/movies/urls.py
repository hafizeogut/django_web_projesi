from django.urls import path
from . import views



urlpatterns = [
    path("",views.index),
    path("movies",views.movies),
    path("movies/<slug:slug>",views.movie_details),#movies altındaki herhangi bir film 
]

#movies/film-adı
#localhost => index.html
#localhost/movies => movies.html 