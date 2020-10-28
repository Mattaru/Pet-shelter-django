from django import forms

from phonenumber_field.formfields import PhoneNumberField

from shelter.models import Pet, Employee, Breed, Owner


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'name',
            'age',
            'description',
            'receipt_date',
            'animal_kind',
            'photo',
            'breed',
            'owner',
        ]


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'position',
            'photo',
        ]


class BreedForm(forms.ModelForm):
    class Meta:
        fields = [
            'name',
            'features',
        ]


class OwnerForm(forms.ModelForm):
    class Meta:
        fields = [
            'first_name',
            'last_name',
            'country',
            'city',
            'street',
            'address',
            'phone_number',
        ]


