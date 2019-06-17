from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )


def dob_validator(value):
    today = date.today()
    if value > today:
        raise ValidationError('Date of birth cannot be in the future.')


class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.PositiveIntegerField(validators=[MaxValueValidator(999999)])
    country = models.CharField(max_length=30)

    #class Meta:
     #ss   unique_together = ("street", "city", "state", "pincode", "country")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(_("Full Name"), max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.PositiveIntegerField(_("Mobile Number"), unique=True, validators=[MaxValueValidator(9999999999)])
    gender = models.CharField(max_length=11, choices=GENDER, null=True)
    profile_pic = models.ImageField(_("profile Picture"), upload_to='profile_pic', null=True, blank=True, default='profile_pic/blank-profile-pic.jpg')
    dob = models.DateField(_("Date of birth"), validators=[dob_validator], null=True)
    permanent_address = models.OneToOneField(Address, null=True, related_name='permanent_address', on_delete=models.SET_NULL, blank=True)
    company_address = models.OneToOneField(Address, null=True, related_name='company_address', on_delete=models.SET_NULL, blank=True)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.username

    