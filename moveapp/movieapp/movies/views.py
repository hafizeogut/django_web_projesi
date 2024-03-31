from django.http import HttpResponse
from django.shortcuts import render 

# Create your views here.
#request,response
#istek,yanıt
def index(request):
    return render(request,'index.html')

#movies listesini gösterecek olacak fonjsiyo
def movies(request):
    return render(request,'movies.html')

def movie_details(request,slug):
    return render(request,'movie_details.html',{
        "slug":slug
    })
