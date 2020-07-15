from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
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

class BookListView(generic.ListView):
	model = Book
	paginate_by = 10
	"""
	context_object_name = 'my_book_list'   # your own name for the list as a template variable
    queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
	"""

class BookDetailView(generic.DetailView):
	model = Book


"""
If not using the generic, method:

def book_detail_view(request, primary_key):
    try:
        book = Book.objects.get(pk=primary_key)
    except Book.DoesNotExist:
        raise Http404('Book does not exist')
    
    return render(request, 'catalog/book_detail.html', context={'book': book})

    or

def book_detail_view(request, primary_key):
	book = get_object_or_404(Book, pk=primary_key)
	return render(request, 'catalog/book_detail.html', context={'book': book})

"""

