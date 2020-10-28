from django.contrib import admin

from shelter.models import Pet, Employee, Breed, Owner


@admin.register(Pet)
class AdminAnimal(admin.ModelAdmin):
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


@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    fields = [
        'first_name',
        'last_name',
        'phone_number',
        'position',
        'photo',
    ]


@admin.register(Breed)
class AdminBreed(admin.ModelAdmin):
    fields = [
        'name',
        'features',
    ]


@admin.register(Owner)
class AdminOwner(admin.ModelAdmin):
    fields = [
        'first_name',
        'last_name',
        'country',
        'city',
        'street',
        'address',
        'phone_number',
    ]