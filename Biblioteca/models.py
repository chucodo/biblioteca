from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    stock = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    birthday = models.DateField()


class Borrow(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    taken = models.DateField()
    brought = models.DateField()
    status = models.CharField(max_length=50, null=True)
