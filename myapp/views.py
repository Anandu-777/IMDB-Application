from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.models import Movie
from django import forms

# Create your views here.



class MovieForm(forms.Form):
    name=forms.CharField()
    language=forms.CharField()
    runtime=forms.IntegerField()
    genre=forms.CharField()
    director=forms.CharField()
    actors=forms.CharField()
    year=forms.IntegerField()

class MovieListView(View):
    
    def get(self, request, *args, **kwargs):
        qs=Movie.objects.all()
        return render(request,"movie_list.html",{"data":qs})
    


# localhost:8000/movies/{pk}/

class MovieDetailView(View):
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=Movie.objects.get(id=id)
        return render(request,"movie_detail.html",{"data":qs})
    
    
# localhost:8000/movies/{pk}/remove/

class MovieDeleteView(View):
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        Movie.objects.get(id=id).delete()
        return redirect("movie-list")




class MovieCreateView(View):
    def get(self, request, *args, **kwargs):
        form=MovieForm()
        return render(request,"movie_add.html",{"form":form})
    
    def post(self, request, *args, **kwargs):
        
        form=MovieForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            Movie.objects.create(**data)
            return redirect("movie-list")
        else:
            return render(request,"movie_add.html",{"form":form})

             
            
        # data={k:v for k,v in request.POST.items()}
        # data.pop("csrfmiddlewaretoken")
        # Movie.objects.create(**data)
        # return redirect("movie-list")
        