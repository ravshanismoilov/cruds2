from django.forms import ModelForm
from .models import Movie


class CreateMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
