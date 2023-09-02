from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Book, Borrow, Student

# Create your views here.


def index():
    return render(request=request, template_name="biblioteca/index.html")


def login(request):
    return ''


class BooksView(generic.ListView):
    template_name = "biblioteca/books.html"
    context_object_name = "book_list"
    
    def get_queryset(self) -> QuerySet[Any]:
        return Book.objects.order_by("-title")[:5]


class BookView(generic.DetailView):
    model = Book
    template_name = "biblioteca/book.html"


def reserve(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    Borrow.book = book
    Borrow.save() 
    book.stock -= 1
    book.save()
    return HttpResponseRedirect(reverse("biblioteca:books"))


def borrows(request):
    return ''
