from django.core.validators import MinLengthValidator
from django.db import models

from accounts.validators import validate_only_letters


class Account(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show'),
    ]
    username = models.CharField(
        max_length = 150,
        unique = True,
    )
    password = models.CharField(
        max_length = 150,
    )
    email = models.EmailField(
        unique = True,
    )
    first_name = models.CharField(
        max_length = 30,
        validators = [
            MinLengthValidator(2),
            validate_only_letters,
        ]
    )
    last_name = models.CharField(
        max_length = 30,
        validators=[
            MinLengthValidator(2),
            validate_only_letters
        ]
    )
    profile_picture = models.URLField(
        blank=True,
        null=True
    )
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default='Do not show'
    )

    def __str__(self):
        return self.username
