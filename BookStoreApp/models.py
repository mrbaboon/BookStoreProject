import datetime

from django.db import models
from django.utils import timezone


class Book(models.Model):
    book_title = models.CharField(max_length=200)
    add_date = models.DateTimeField('date added')

    def was_added_recently(self):
        return self.add_date >= timezone.now() - datetime.timedelta(days=1)
    was_added_recently.admin_order_field = 'add_date'
    was_added_recently.boolean = True
    was_added_recently.short_description = 'Added Recently?'

    def __str__(self):
        return self.book_title

class BookReview(models.Model):
    book = models.ForeignKey(Book)
    review_text = models.CharField(max_length=800)
    rating_choices=(
        (1, "1 star"),
        (2, "2 stars"),
        (3, "3 stars"),
        (4, "4 stars"),
        (5, "5 stars"),
    )
    rating = models.IntegerField(choices=rating_choices, default=5)


    def __str__(self):
        return self.review_text
