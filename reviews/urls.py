from django.contrib import admin
from django.urls import path

from reviews.views import (ReviewCreate,
                           ReviewList,
                           ReviewUpdate,
                           ReviewDelete,)


app_name = 'reviews'

urlpatterns = [
    path('review/create/', ReviewCreate.as_view(), name='review_create'),
    path('review/', ReviewList.as_view(), name='review_list'),
    path('review/<str:pk>/', ReviewUpdate.as_view(), name='review_update'),
    path('review/<str:pk>/delete/', ReviewDelete.as_view(), name='review_delete'),
]