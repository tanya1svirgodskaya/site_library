"""
Definition of views.
"""


from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .models import Genre



def index (request):
    menu=[('Головна', "#yak1"),('Сервіс',"#yak2"),('Про нас',"#yak3"),('Контакты',"#yak4")]
    mydatetime= datetime.now()
    tit='Вітаємо в LiBook!'
    return render (request,'index2.html',{'tit':tit, 'menu':menu,'mydatetime':mydatetime})



@csrf_exempt
def authors(request):
    if request.method == 'GET': 
        return render(request, 'form.html')
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        second_name=request.POST["second_name"]
        patr=request.POST["patr"]
        year=request.POST["year"]
        newAuthor = Author(first_name=first_name, second_name=second_name,patr_name=patr, birth=year)
        newAuthor.save()
        authors = Author.objects.order_by('-birth')
        return render(request, 'form.html', {'authors': authors })
@csrf_exempt
def publish(request):
    if request.method == 'GET': 
        return render(request, 'formpubl.html')
    if request.method == 'POST':
        name_publish = request.POST["name_publish"]
        address=request.POST["address"]
        phone=request.POST["phone"]
        newPublishing_house=Publishing_house(name=name_publish, address=address,phone=phone)
        newPublishing_house.save()
        publishes=Publishing_house.objects.order_by('id')
        return render(request, 'formpubl.html', {'publishes': publishes })

@csrf_exempt
def genre(request):
    if request.method == 'GET': 
        return render(request, 'formgenre.html')
    if request.method == 'POST':
        name=request.POST["name"]
        newGenre=Genre(name=name)
        newGenre.save()
        genres=Genre.objects.order_by('id')
        return render(request, 'formgenre.html', {'genres': genres })

@csrf_exempt
def book(request):
    if request.method == 'GET':
        p=Publishing_house.objects.raw("SELECT * FROM TNBooks_publishing_house")
        return render(request, 'Book.html', {'publish':p})
    if request.method == 'POST':
        name= request.POST ['name']
        year=request.POST['year']
        annotation=request.POST['annotation']
        publ=request.POST ['publ']
        publish= Publishing_house.objects.get(id=publ)
        newBook=Books(name=name, publish=publish ,year=year,annotation=annotation )
        newBook.save()
        p=Publishing_house.objects.raw("SELECT * FROM TNBooks_publishing_house")
        authorb=Author_books.objects.raw("SELECT * FROM TNBooks_author_books")
        author=Author.objects.raw("SELECT * FROM TNBooks_author")
        b=Books.objects.raw("SELECT * FROM TNBooks_books WHERE year> 1800 GROUP BY name ORDER BY id ")
        return render(request, 'Book.html', {'publish':p,'book':b , 'authorb':authorb, 'author':author})
@csrf_exempt
def b(request):
    if request.method == 'GET':
        p=Books.objects.raw("SELECT * FROM TNBooks_books")
        a=Author.objects.raw("SELECT * FROM TNBooks_author")
        return render(request, 'b.html', {'aut':a,'bo': p})
    if request.method == 'POST':
        p=Books.objects.raw("SELECT * FROM TNBooks_books")
        a=Author.objects.raw("SELECT * FROM TNBooks_author")
        id_book= request.POST ['kn']
        id_author=request.POST['au']
        book= Books.objects.get(id=id_book)
        author=Author.objects.get(id=id_author)
        newBook_author=Author_books(id_author=author, id_book=book )
        newBook_author.save()
        k=Author_books.objects.raw("SELECT * FROM TNBooks_author_books")
        return render(request, 'b.html', {'aut':a,'bo': p,'book':k})