from django.contrib import admin
from django.urls import path

from shelter.views import (HomePage,
                           AboutUsPage,
                           TroublesWithPetsPage,
                           FindHomelessPetPage,
                           PetList,
                           PetCreate,
                           PetDetail,
                           PetDelete,
                           PetUpdate,
                           EmployeeList,
                           EmployeeCreate,
                           EmployeeUpdate,
                           EmployeeDelete,
                           EmployeeDetail,)


app_name = 'shelter'

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('about_us/', AboutUsPage.as_view(), name='about_us'),
    path('troubles/', TroublesWithPetsPage.as_view(), name='troubles_pet'),
    path('find_homeless/', FindHomelessPetPage.as_view(), name='find_homeless'),

    path('pet/create/', PetCreate.as_view(), name='pet_create'),
    path('pet/', PetList.as_view(), name='pet_list'),
    path('pet/<str:pk>/', PetDetail.as_view(), name='pet_detail'),
    path('pet/<str:pk>/update/', PetUpdate.as_view(), name='pet_update'),
    path('pet/<str:pk>/delete/', PetDelete.as_view(), name='pet_delete'),

    path('employee/create/', EmployeeCreate.as_view(), name='employee_create'),
    path('employee/', EmployeeList.as_view(), name='employee_list'),
    path('employee/<str:pk>/', EmployeeDetail.as_view(), name='employee_detail'),
    path('employee/<str:pk>/update/', EmployeeUpdate.as_view(), name='employee_update'),
    path('employee/<str:pk>/delete/', EmployeeDelete.as_view(), name='employee_delete'),
]