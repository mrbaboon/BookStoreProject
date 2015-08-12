from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book

def index(request):
    latest_book_list = Book.objects.order_by('-add_date')[:5]
    context = {'latest_book_list': latest_book_list}
    return render(request, 'BookStoreApp/index.html', context)

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'BookStoreApp/detail.html', {'book': book})

def results(request, book_id):
    response =  "You're looking at the reviews of %s."
    return HttpResponse(response % book_id)

def rate(request, book_id):
    return HttpResponse("You're rating book %s" % book_id)