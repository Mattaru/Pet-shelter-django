from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView,
                                  ListView,
                                  UpdateView,
                                  DeleteView,)

from reviews.forms import ReviewForm
from reviews.models import Review


class ReviewCreate(CreateView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('reviews:review_list')
    template_name = 'pages/reviews/ReviewCreate.html'


class ReviewList(ListView):
    model = Review
    template_name = 'pages/reviews/ReviewList.html'


class ReviewUpdate(UpdateView):
    model = Review
    fields = [
        'author_name',
        'title',
        'message_data',
    ]
    success_url = reverse_lazy('reviews:review_list')
    template_name = 'pages/reviews/ReviewUpdate.html'


class ReviewDelete(DeleteView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('reviews:review_list')
    template_name = 'pages/reviews/ReviewDelete.html'



