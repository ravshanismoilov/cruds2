from django.shortcuts import render, redirect
from .models import Category, Movie
from .forms import CreateMovieForm


def home_page(request):
    return render(request, 'home.html')

def category_movie(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'movie/category_movie.html', context=context)

def detail_category(request, pk):
    category = Category.objects.get(pk=pk)
    movies = Movie.objects.filter(category=pk)
    context = {
        'movies': movies,
        'category': category
    }
    return render(request, 'movie/detail_category.html', context=context)

def detail_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }
    return render(request, 'movie/detail_movie.html', context=context)

def create_movie(request):
    create_form = CreateMovieForm(data=request.POST, files=request.FILES)
    if request.method == 'POST':
        if create_form.is_valid():
            create_form.save()
            return redirect('category-movie')
    context = {
        'create_form': create_form
    }
    return render(request, 'movie/create_movie.html', context=context)

def delete_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }
    if movie:
        movie.delete()
        return redirect('detail-category', movie.category_id)
    return render(request, 'movie/delete_movie.html', context=context)

def update_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    update_form = CreateMovieForm(data=request.POST, files=request.FILES, instance=movie)
    if request.method == 'POST':
        if update_form.is_valid():
            update_form.save()
            return redirect('detail-movie', movie.pk)
    context = {
        'update_form': update_form,
        'movie': movie
    }
    return render(request, 'movie/update_movie.html', context=context)