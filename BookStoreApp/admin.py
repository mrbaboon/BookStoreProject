from django.contrib import admin
from .models import Book, BookReview

class BookReviewInline(admin.TabularInline):
    model = BookReview

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['book_title']}),
        ('Date information',  {'fields': ['add_date']}),
    ]
    inlines = [BookReviewInline]
    list_display = ('book_title', 'add_date', 'was_added_recently')
    list_filter = ['add_date']
    search_fields = ['book_title']

admin.site.register(Book, BookAdmin)
