from django.urls import path
from . import views

urlpatterns = [
	path('books/', views.books, name="task-list"),
	path('book-detail/<str:pk>/', views.book_detail, name="book-detail"),
	path('create-book/', views.create_book, name="create-book"),

	path('update-book/<str:pk>/', views.update_book, name="update-book"),
	path('delete-book/<str:pk>/', views.delete_book, name="delete-book"),
]
