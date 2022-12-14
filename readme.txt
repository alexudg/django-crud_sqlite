##### Prerequisites:
  * windows 7 x64 sp1

  * python 3 & pip, comprobation:
    > python --version
    Python 3.8.6

    > pip --version
    pip 21.3.1
  
  * extensions vscode:
    - bootstrap quick snnipets 5
    - python

##### install django
  > pip install Django
  Successfully installed Django-4.1 asgiref-3.5.2 backports.zoneinfo-0.2.1 sqlparse-0.4.2 tzdata-2022.2

  * Comprobation:
    > django-admin --version
    4.1

##### create project Django
  > django-admin startproject <name_project> 

  created project folder with db:
  
  <name_project>
  |
  +--<name_project>
  |  |
  |  + *.py
  |
  +--db.sqlite3
  +--manage.py  

##### run server for comprobation:
  # cd <name_project>

  # run 
    > python3 manage.py runserver

##### create app of project
  * inside of project folder, create app:
    > python manage.py startapp main   
    
    <name_project>/
    |
    +--<name_project>/
    |  |
    |  +--*.py (various)
    |
    +--main/
    |  |
    |  +--migrations/
    |  |  |
    |  |  +--*.py (various)
    |  |
    |  +--*.py (various)
    |
    +--db.sqlite3
    +--manage.py  

  * register app on file '<name_project>\<name_project>\settings'  

    ...
    INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'main'  <=========== here
    ]
    ...
        
##### create view editing file '<project>\main\views.py'        

...
from django.http import HttpResponse
...

def index(req):
    return HttpResponse('<h1>Hello world!</h1>')

##### create router of app 'main' with on new file '<project>\main\urls.py'

from django.urls import path
from . import views # . = here

urlpatterns = [
    path('', views.index, name='inicio') # '' = '/'
]

##### create router global to app on file '<project>\<project>\urls.py':

...
from django.urls import include
...

urlpatterns = [
    ...
    path('', include('main.urls')) # <== added new path global '' = '/'
]

verify runing server

##### create templates on new folder required '<project>\main\templates'

  * into folder 'templates' create new folder 'pages' or custom name (not required);
    into folder 'pages' create 2 html files o more

  <project>/
  |
  +--main/
  | |
  | +--...
  | |
  | +--templates/  <== required folder
  | |  |
  | |  +--pages/  <== custom folder with custom html files
  | |     |
  | |     +--index.html  
  | |     +--we.html  
  | |  
  | +--(various *.py)   

##### binding templates to views

  # file 'views':

    ... 
    from django.shortcuts import render

    ...
    def we(req):
      return render(req, 'pages/we.html') # search on folder 'templates' automatic

  # file '<project>\main\urls.py':

    from django.urls import path
    from . import views # . = here

    urlpatterns = [
        path('', views.index, name='inicio'),
        path('we', views.we, name='we') # <== new binding
    ]    

##### create template global named '<project>\main\template\base.html' 
  with 3 blocks django: before <!doctype html>, into <title>, into <div class='container'>     

  * with help of extension 'bootstrap5' only type 'bs5-$' created new document html 
    with bootstrap5, also: add container into label <main>

  {% load static %}  <!-- block django -->
  <!doctype html>
  <html lang="es">

  <head>
      <title>{% block title %} {% endblock %}</title> <!-- block django -->
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

      <!-- Bootstrap CSS v5.2.0-beta1 -->
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css"
          integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">

  </head>

  <body>
      <header>
          <!-- place navbar here -->
      </header>
      <main>
          <div class="container">
              <div class="row">
                  <div class="col-12">
                    {% block container %} {% endblock %} <!-- block django -->
                  </div>
              </div>
          </div>
      </main>
      <footer>
          <!-- place footer here -->
      </footer>

      <!-- Bootstrap JavaScript Libraries -->
      <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js"
          integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous">
          </script>

      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.min.js"
          integrity="sha384-ODmDIVzN+pFdexxHEHFBQH3/9/vQ9uori45z4JjnFsRydbmQbmL5t1tQ0culUzyK" crossorigin="anonymous">
          </script>
  </body>

  </html>

##### create pages inserting template 'base.html':

  {% extends 'base.html' %} <!-- include template 'base.html' -->

  {% block title %} Inicio {% endblock %} <!-- insert into block 'title' of 'base.html' -->

  {% block container %} Seccion de Inicio {% endblock %} <!-- insert into block 'container' of 'base.html' -->

##### if insert other template as a form use 'include'

  {% extends 'base.html' %} <!-- include template 'base.html' -->

  {% block title %} Inicio {% endblock %} <!-- insert into block 'title' of 'base.html' -->

  {% block container %} 
  
  {% include 'pages/books/form.html' %} <!-- insert here 'form.html' from 'templates\' -->
  
  {% endblock %} <!-- insert into block 'container' of 'base.html' -->

  #####  config database on file '<project>\<project>\settings.py', example for mysql

    ...
    DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypass',
        'HOST': '127.0.0.1',
        'PORT': '3306'
      }
    }
    ...

    If use myssql, edit file '<project>\<project>\__init__.py':

    import pymysql
    pymysql.install_as_MySQLdb()

##### crate model of table db on '<project>\main\models.py'  

  from django.db import models

  # Create your models here.

  class Libro(models.Model):
      id = models.AutoField
      title = models.CharField(max_length=128, verbose_name='Titulo') # verbose_name = label on form
      image = models.ImageField(upload_to='images/', null=True, verbose_name='Imagen')
      description = models.TextField(null=True, verbose_name='Descripcion')
  
  # create migrations and migrate for create table
    > python manage.py makemigrations
    > python manage.py migrate

  # tables results:
    - auth_group
    - auth_group_permissions
    - auth_permissions
    - auth_user
    - auth_user_groups
    - auth_user_user_permissions
    - django_admin_log
    - django_content_type
    - django_migrations
    - django_session
    - main_libro   <=========== this is the previos model 
      |
      +--id integer PK not null autoincrement
      +--title varchar(128) not null
      +--image varchar(100)
      +--description text

##### config admin for create interfaz for editing table on file '<project>\main\admin.py'
  from django.contrib import admin
  from .models import Book

  admin.site.register(Book)

  # create super-user:
    > python manage.py createsuperuser
      Username: alexudg
      Email address: alexudg@gmail.com
      Password: 1
      Password (again): 1
      This password is too short. It must contain at least 8 characters.
      This password is too common.
      This password is entirely numeric.
      Bypass password validation and create user anyway? [y/N]: y

  # comprobation:
    > python manage.py runserver   

    * on navigator get  http://127.0.0.1:8000/admin/ 
    * enter nue username & password previous
    * dispose of model Book for add, edit & delete books

##### edit 'main\models.py' for add property __str__ and delete image when delete book 

    # show this string on list of books of admin, replacing  Object(x) by title: <title>, description: <description>
    def __str__(self):
        row = 'Título: ' + self.title + ', Descripción: ' + self.description
        return row
          
    # this force to delete image from storage
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()   

##### edit 'main\views.py' for send array of objects books to view of list of books

  ...
  from .models import Book

  ...
  def books(req):
    books = Book.objects.all() # <== get all books and pass as object
    print(books) # comprobation
    return render(req, 'pages/books/list.html', {'books': books}) # search on folder 'templates' automatic

##### edit template 'main\templates\books\list.html' for create table:

  ...
  <tbody>
    {% for book in books %} <!-- books import from views.py { 'books': books } -->
    <tr class="">
        <td>{{ book.id }}</td> <!-- doubles '{{' '}}' without '%' -->
        <td>{{ book.title }}</td>
        <td><img src="{{ book.image.url }}" alt="{{ book.title }}" width="100" height="60"></td>
        <td>{{ book.description }}</td>
        <td>
            <a class="btn btn-info text-white" href="{% url 'update' %}" role="button">Modificar</a> | 
            <a class="btn btn-danger text-white" href="#" role="button">Eliminar</a>
        </td>
    </tr> 
    {% endfor %}                   
  </tbody>

  ##### config for show images without lock of django 
    
    # add lines on <project>\settings.py

    ...
    import os

    ...
    MEDIA_ROOT = os.path.join(BASE_DIR, '') # <fullpath_project>/
    MEDIA_URL = 'images/' 

    # add lines on main\urls.py

    ...
    from django.conf import settings
    from django.contrib.staticfiles.urls import static

    ...
    urlpatterns = [
        ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # <== add this line

##### create structure of form and method insert
  
    # create file <project>\main\forms.py

      from django import forms
      from .models import Book

      class BookForm(forms.ModelForm):
          class Meta:
              model = Book
              fields = '__all__'

    # edit file 'main\views.py'

      ...
      from django.shortcuts import render, redirect # <== add 'redirect'
      from .forms import BookForm # <== use form for insert/update

      ...
      def insert(req):
        bookForm = BookForm(req.POST or None, req.FILES or None) # <== create form type post
        #print(bookForm) # <== comprobate (html code)
        #print('isValid: ', bookForm.is_valid()) # comprobate
        if bookForm.is_valid():
            bookForm.save()
            return redirect('books') # urls.py -> path(..., name='books')
        return render(req, 'pages/books/insert.html', { 'bookForm': bookForm }) # send form on object
    
    # edit main\templates\books\form.py
    
      <form enctype="multipart/form-data" method="post">
        
        <!-- input hidden secret from django -->
        {% csrf_token %}
        
        {% for field in bookForm %}

        <!-- fields on table -->
        <div class="mb-3">
            <label for="title" class="form-label">{{ field.label }}</label>
            <input 
                type="{{ field.field.widget.input_type }}" 
                class="form-control" 
                name="{{ field.name }}"
                id=""
                placeholder="{{ field.label }}" 
            />
            <!-- id: asigned automatic -->
        </div>
        <small class="col-12 form-text text-danger">{{ field.errors }}</small>

        {% endfor %}
        
        <!-- <input class="btn btn-primary" type="button" value="Guardar"> -->
        <input type="submit" value="Guardar">
      </form>

##### config for delete row and refresh

  # add function 'main\views.py'

    def delete(req, id): # <== add id param
      book = Book.objects.get(id=id)
      #print(book) # comprobation
      book.delete()
      return redirect('books')

  # add url line on 'main\urls.py'

    ...
    urlpatterns = [
      ...
      path('eliminar/<int:id>', views.delete, name='delete'), # <== include /id
      ...
    ] + ...  

  # edit line href on 'main\templates\pages\books\list.html'

    ...
    <!-- send id in 'href' -->
    <a 
      class="btn btn-danger text-white" 
      href="{% url 'delete' book.id %}" 
      role="button">
      Eliminar
    </a>
    ...  

##### config update book

  # edit function update on main\views.py

    def update(req, id):
      book = Book.objects.get(id=id)
      #print(book) # comprobation
      bookForm = BookForm(req.POST or None, req.FILES or None, instance=book) # important instance
      if bookForm.is_valid() and req.POST:
          bookForm.save()
          return redirect('books')
      return render(req, 'pages/books/update.html', { 'bookForm': bookForm }) # search on folder 'templates' automatic

  # add url line on 'main\urls.py'

    ...
    urlpatterns = [
      ...
      path('update/<int:id>', views.update, name='update'), # <== include /id
      ...
    ] + ...    

  # edit line href on 'main\templates\pages\books\list.html'

    ...
    <!-- send id in 'href' -->
    <a 
      class="btn btn-primary text-white" 
      href="{% url 'update' book.id %}" 
      role="button">
      Modificar
    </a>
    ...    

  # edit line href on 'main\templates\pages\books\form.html' 
    
    {% for field in bookForm %}

    <div class="mb-3">
      <label for="title" class="form-label">{{ field.label }}</label>

      <!-- SHOW case of UPDATE -->
      {% if field.field.widget.input_type == 'file' and field.value %}
          <img 
              src="{{ MEDIA_URL }}/images/{{ field.value }}" 
              alt="{{ field.label }}" 
              width="35" 
              height="50" 
              class="mb-3" />
      {% endif %}

      <!-- ADD value both cases INSERT/UPDATE -->
      <input 
          type="{{ field.field.widget.input_type }}" 
          class="form-control" 
          name="{{ field.name }}"
          id=""
          placeholder="{{ field.label }}" 
          value="{{ field.value | default:'' }}"                
      />
      <!-- id: asigned automatic -->
  </div>
  <small class="col-12 form-text text-danger">{{ field.errors }}</small>
  
  {% endfor %} 