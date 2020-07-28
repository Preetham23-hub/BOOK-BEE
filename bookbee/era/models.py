from django.db import models


class Register(models.Model):
    username=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=20)


class Upload(models.Model):
    name=models.CharField(max_length=50)
    file=models.FileField()

class Pdf(models.Model):

    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    pdf= models.FileField(upload_to='media/books/pdf')
    sname=models.CharField(max_length=50)
    image=models.ImageField(upload_to='media/books/img',default='media/img/book.jpg')

    def __str__(self):
      return self.title


