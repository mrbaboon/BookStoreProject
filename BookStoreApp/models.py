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
    rating = models.IntegerField(default = 5)

    def __str__(self):
        return self.review_text
