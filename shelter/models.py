from django.db import models
from django.urls import reverse
from django.core import validators

from phonenumber_field.modelfields import PhoneNumberField


class Owner(models.Model):
    first_name = models.CharField(verbose_name='First name', max_length=50)
    last_name = models.CharField(verbose_name='Last name', max_length=50)
    country = models.CharField(verbose_name='Country', max_length=30)
    city = models.CharField(verbose_name='City', max_length=30)
    street = models.CharField(verbose_name='Street', max_length=40)
    address = models.CharField(verbose_name='Address', max_length=60)
    phone_number = PhoneNumberField(verbose_name='Phone number', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} from {self.country} (num: {self.phone_number})'


class Employee(models.Model):
    first_name = models.CharField(verbose_name='First name', max_length=50)
    last_name = models.CharField(verbose_name='Last name', max_length=50)
    phone_number = PhoneNumberField(verbose_name='Phone number', blank=True)
    WORK_POSITION = [
        ('MANAGER', 'Manager'),
        ('PRESIDETN', 'President'),
        ('VICE PRESIDENT', 'Vice president'),
        ('MANAGER', 'Manager'),
        ('TRAINEE', 'Trainee'),
    ]
    position = models.CharField(verbose_name='Position', max_length=50,
                                choices=WORK_POSITION, default='Trainee')
    photo = models.ImageField(verbose_name='Photo', upload_to='employees_photo/',
                              default='unknown.png')

    def __str__(self):
        return " ".join([
            str(self.first_name),
            str(self.last_name)
        ])


class Breed(models.Model):
    name = models.CharField(verbose_name='name', max_length=50)
    features = models.TextField(verbose_name='Features', max_length=1500)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    age = models.IntegerField(verbose_name='Age', validators=[validators.MaxValueValidator(30)])
    description = models.TextField(verbose_name='Description', max_length=1500)
    receipt_date = models.DateField(verbose_name='Receipt date')
    KIND_OF_ANIMAL = [
        ('UNKNOWN', 'Unknown'),
        ('CAT', 'Cat'),
        ('DOG', 'Dog'),
        ('HAMSTER', 'Hamster'),
        ('RABBIT', 'Rabbit'),
        ('PARROT', 'Parrot'),
    ]
    animal_kind = models.CharField(verbose_name='Animal kind', max_length=10,
                                   choices=KIND_OF_ANIMAL, default='UNKNOWN')
    photo = models.ImageField(verbose_name='Photo', upload_to='animals_photo/',
                              default='unknown.png')
    breed = models.ForeignKey('shelter.Breed', verbose_name='Breed', null=True, blank=True,
                              on_delete=models.SET_NULL, related_name='pet_breed')
    owner = models.ForeignKey('shelter.Owner', verbose_name='Owner', null=True, blank=True,
                              on_delete=models.SET_NULL, related_name='pet_owner')

    def __str__(self):
        return f'{self.name} ({self.animal_kind} - {self.breed} - {self.age} years old)'

    def get_absolute_url(self):
        return reverse('pet_detail', kwargs={'pk': self.pk})











