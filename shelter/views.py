from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import (ListView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView,
                                  DetailView,)

from shelter.models import Pet, Employee
from shelter.forms import PetForm, EmployeeForm


class HomePage(TemplateView):
    template_name = 'pages/home/home.html'


class AboutUsPage(TemplateView):
    template_name = 'pages/about-us/aboutUs.html'


class TroublesWithPetsPage(TemplateView):
    template_name = 'pages/home/TroublesPet.html'


class FindHomelessPetPage(TemplateView):
    template_name = 'pages/home/FindPet.html'


class PetCreate(CreateView):
    model = Pet
    form_class = PetForm
    success_url = reverse_lazy('shelter:pet_list')
    template_name = 'pages/our-pets/PetCreate.html'


class PetList(ListView):
    model = Pet
    template_name = 'pages/our-pets/PetList.html'

    def get_queryset(self):
        qs = super().get_queryset()
        get_params = self.request.GET.dict()

        if get_params.get('petSearch'):
            qs = qs.filter(name__icontains=get_params.get('petSearch'))

        return qs


class PetUpdate(UpdateView):
    model = Pet
    fields = [
        'name',
        'age',
        'receipt_date',
        'animal_kind',
        'photo',
        'breed',
        'description',
    ]
    success_url = reverse_lazy('shelter:pet_list')
    template_name = 'pages/our-pets/PetUpdate.html'


class PetDelete(DeleteView):
    model = Pet
    form_class = PetForm
    success_url = reverse_lazy('shelter:pet_list')
    template_name = 'pages/our-pets/PetDelete.html'


class PetDetail(DetailView):
    model = Pet
    template_name = 'pages/our-pets/PetDetail.html'


class EmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('shelter:employee_list')
    template_name = 'pages/employees/EmployeeCreate.html'


class EmployeeList(ListView):
    model = Employee
    template_name = 'pages/employees/EmployeeList.html'

    def get_queryset(self):
        qs = super().get_queryset()
        get_params = self.request.GET.dict()

        if get_params.get('employeeSearch'):
            qs = qs.filter(last_name__icontains=get_params.get('employeeSearch'))

        return qs


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = [
        'first_name',
        'last_name',
        'phone_number',
        'position',
        'photo',
    ]
    success_url = reverse_lazy('shelter:employee_list')
    template_name = 'pages/employees/EmployeeUpdate.html'


class EmployeeDelete(DeleteView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('shelter:employee_list')
    template_name = 'pages/employees/EmployeeDelete.html'


class EmployeeDetail(DeleteView):
    model = Employee
    template_name = 'pages/employees/EmployeeDetail.html'