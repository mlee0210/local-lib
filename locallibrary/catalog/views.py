from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
# Create your views here.

def index(request):
	#View function for homepage

	#generate counts of some of the main objects
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()

	#Available books(which has status = 'a')
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()

	num_authors = Author.objects.count()  #.all() is implied by default

	#to filter for books with a specific genre pattern, you will have to index to the name through the genre field
	num_romance_books = Book.objects.filter(genre__name__icontains='Romance').count()

	num_harry_books = Book.objects.filter(title__icontains='harry').count()

	context = {
		'num_books': num_books,
		'num_instances': num_instances,
		'num_instances_available': num_instances_available,
		'num_authors': num_authors,
		'num_romance_books': num_romance_books,
		'num_harry_books': num_harry_books,

	}
	#render HTML template index.html with data in 'context' variable
	return render(request, 'index.html', context=context)
