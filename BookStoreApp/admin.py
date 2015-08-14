from django.contrib import admin

from .models import Author, Book, BookReview

class BookReviewInline(admin.StackedInline):
    model = BookReview

class BookAdmin(admin.ModelAdmin):
    inlines = [BookReviewInline]

class BookInline(admin.StackedInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
