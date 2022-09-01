from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=128, verbose_name='Titulo') # verbose_name = field.label on form
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Imagen')
    description = models.TextField(null=True, verbose_name='Descripcion')

    # show this string on list of admin
    def __str__(self):
        row = 'Titulo: ' + self.title + ', Descripcion: ' + self.description
        return row

    # this force to delete image from storage
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()    