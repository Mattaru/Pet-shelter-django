from django.contrib import admin

from reviews.models import Review


@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    fields = [
        'author_name',
        'title',
        'message_data',
    ]
