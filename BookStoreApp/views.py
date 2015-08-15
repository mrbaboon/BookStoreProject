from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render

from .models import Book, Author, BookReview

def index(request):
    book_list = Book.objects.order_by('-book_title')[:5]
    context = {'book_list': book_list}
    return render(request, 'BookStoreApp/index.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'BookStoreApp/book_detail.html', context)

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {'author': author}
    return render(request, 'BookStoreApp/author_detail.html', context)

def book_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    new_review = book.bookreview_set.create(review_text=request.POST['review'], stars=request.POST['stars'])
    stars = avg_book_stars(book_id)
    context = {'book':book, 'stars':stars}
    return render(request, 'BookStoreApp/book_detail.html', context)

def avg_book_stars(book_id):
    book = get_object_or_404(Book, pk=book_id)
    count = 0
    stars = 0
    for review in book.bookreview_set.all():
        stars = review.stars + stars
        count += 1
    stars = (2*stars) // count
    stars = stars/2 # This makes stars round to the nearest half integer
    return stars