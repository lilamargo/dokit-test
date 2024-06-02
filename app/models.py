from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class DoctorManager(BaseUserManager):
    def create_user(self, email, names, first_lastname, second_lastname, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            names=names,
            first_lastname=first_lastname,
            second_lastname=second_lastname,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, names, first_lastname, second_lastname, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, names, first_lastname, second_lastname, phone_number, password, **extra_fields)

class Doctor(AbstractBaseUser):
    email = models.EmailField(unique=True)
    names = models.CharField(max_length=100)
    first_lastname = models.CharField(max_length=100)
    second_lastname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    main_office_address = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['names', 'first_lastname', 'second_lastname', 'date_of_birth', 'main_office_address']

    objects = DoctorManager()


class Office(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    ext_number = models.CharField(max_length=100, null=True)
    int_number = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=8)
    neighborhood = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
