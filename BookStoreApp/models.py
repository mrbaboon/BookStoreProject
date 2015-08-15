from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name + ", " + self.first_name

class Book(models.Model):
    author = models.ForeignKey(Author)
    book_title = models.CharField(max_length=100)

    def __str__(self):
        return self.book_title

class BookReview(models.Model):
    book = models.ForeignKey(Book)
    stars = models.IntegerField()
    review_text = models.CharField(max_length=200)

    def __str__(self):
        return self.review_text