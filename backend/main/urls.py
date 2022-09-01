from django.urls import path
from . import views  # . = here

# for show images from path
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.index, name='index'),  # '' = '/' | name for <a href> & redirect()
    path('libros', views.books, name='books'),
    path('agregar', views.insert, name='insert'),
    path('modificar/<int:id>', views.update, name='update'),
    path('eliminar/<int:id>', views.delete, name='delete'),
    path('nosotros', views.we, name='we')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # <== add this line

