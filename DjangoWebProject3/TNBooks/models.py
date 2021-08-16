"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Author(models.Model):
    first_name= models.CharField (max_length=50, verbose_name='Имя')
    second_name= models.CharField(max_length=50, db_index=True, verbose_name='Фамилия')
    patr_name= models.CharField(max_length=50,  verbose_name='Отчество')
    birth= models.CharField(max_length=4,  verbose_name='Год рождения')
class Publishing_house(models.Model):
   name= models.CharField(max_length=20, db_index=True, verbose_name='Название')
   address= models.CharField(max_length=70,  verbose_name='Адрес')
   phone= models.CharField(max_length=20, verbose_name='Номер телефона')

class Genre(models.Model):
   name= models.CharField(max_length=20, db_index=True, verbose_name='Название жанра')
  
class Books(models.Model):
   name= models.CharField(max_length=20, db_index=True, verbose_name='Название')
   publish= models.ForeignKey(Publishing_house, on_delete=models.PROTECT)
   year= models.CharField(max_length=4,  verbose_name='Год выпуска')
   annotation= models.CharField(max_length=255,  verbose_name='Аннотация')
   class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'
        ordering = ['year']
class Genre_books  (models.Model):
   id_genre= models.ForeignKey(Genre, on_delete=models.PROTECT)
   id_book= models.ForeignKey(Books, on_delete=models.PROTECT)
class Author_books(models.Model):
   id_author= models.ForeignKey(Author, on_delete=models.PROTECT)
   id_book= models.ForeignKey(Books, on_delete=models.PROTECT, verbose_name='Книга')
