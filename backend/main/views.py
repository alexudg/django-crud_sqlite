from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm # <== use form for insert/update

# Create your views here.

def index(req):
    return render(req, 'pages/index.html') # search on folder 'templates' automatic

def books(req):
    books = Book.objects.all() # <== get all rows 
    #print(books) # comprobation
    return render(req, 'pages/books/list.html', {'books': books}) # search on folder 'templates' automatic  

def insert(req):
    bookForm = BookForm(req.POST or None, req.FILES or None) # <== create form type post
    #print(bookForm) # <== comprobate (html code)
    #print('isValid: ', bookForm.is_valid()) # comprobate
    if bookForm.is_valid():
        bookForm.save()
        return redirect('books') # urls.py -> path(..., name='books')
    return render(req, 'pages/books/insert.html', { 'bookForm': bookForm }) # send form on object

def update(req, id):
    book = Book.objects.get(id=id)
    #print(book) # comprobation
    bookForm = BookForm(req.POST or None, req.FILES or None, instance=book)
    if bookForm.is_valid() and req.POST:
        bookForm.save()
        return redirect('books')
    return render(req, 'pages/books/update.html', { 'bookForm': bookForm }) # search on folder 'templates' automatic

def delete(req, id):
    book = Book.objects.get(id=id)
    print(book) # comprobation
    book.delete()
    return redirect('books')

def we(req):
    return render(req, 'pages/we.html') # search on folder 'templates' automatic
