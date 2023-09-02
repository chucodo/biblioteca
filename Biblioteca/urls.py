from django.urls import path
from . import views

app_name = "biblioteca"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("books/", views.BooksView.as_view(), name="books"),
    path("book/<int:pk>", views.BookView.as_view(), name="book"),
    path("book/reserve/<int:book_id>", views.reserve, name="reserve"),
    path("borrows/", views.borrows, name="borrows")

]
