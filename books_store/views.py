from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer

from .models import Book

# Getting all books
@api_view(['GET'])
def books(request):
	tasks = Book.objects.all().order_by('-id')
	serializer = BookSerializer(tasks, many=True)
	return Response(serializer.data)


# Getting one book
@api_view(['GET'])
def book_detail(request, pk):
	tasks = Book.objects.get(id=pk)
	serializer = BookSerializer(tasks, many=False)
	return Response(serializer.data)


# Adding new book
@api_view(['POST'])
def create_book(request):
	serializer = BookSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


# Updating existing book
@api_view(['POST'])
def update_book(request, pk):
	task = Book.objects.get(id=pk)
	serializer = BookSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


# Deleting a book
@api_view(['DELETE'])
def delete_book(request, pk):
	task = Book.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')



