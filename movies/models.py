from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=155)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'language'

    def __str__(self):
        return self.name


class Movie(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)
    film_name = models.CharField(max_length=155)
    language = models.ForeignKey(to=Language, on_delete=models.SET_NULL, null=True)
    time = models.IntegerField()
    about = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='', blank=True, null=True)

    class Meta:
        db_table = 'movie'

    def __str__(self):
        return f'{self.category.name} - {self.film_name}, {self.time} minutes'



class Review(models.Model):
    body = models.TextField()
    star_given = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)

    class Meta:
        db_table ='review'

    def __str__(self):
        return f'{self.movie.film_name} - {self.star_given} - {self.user}'
