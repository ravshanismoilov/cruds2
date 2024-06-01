from django.db import models


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
