from django.contrib import admin
from .models import Author, Book, Student, Borrow, Category

# Register your models here.

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Borrow)
