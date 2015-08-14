from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render

from .models import Book, Author

def index(request):
    book_list = Book.objects.order_by('-book_title')[:5]
    context = {'book_list': book_list}
    return render(request, 'BookStoreApp/index.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    print("book id is " + book_id)
    print("book is " + book.book_title)
    context = {'book': book}
    return render(request, 'BookStoreApp/book_detail.html', context)

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return HttpResponse("You're looking at %s." % author)

