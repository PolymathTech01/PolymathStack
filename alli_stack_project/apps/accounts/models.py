from multiprocessing.managers import BaseManager
from typing import Any, List
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomerUserManager
from django.template.defaultfilters import slugify
from . import utils
# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    slug = models.SlugField(unique=True, blank=True)

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS: List[str] = []

    objects: Any = CustomerUserManager()

    class Meta:
        ordering = ['email']
        verbose_name = 'User'

    def __str__(self):
        return self.email

    # Creating a default slug/username for users if blank.

    def generate_random_slug(self):

        random_slug = slugify(
            self.first_name + self.last_name + utils.generate_random_id())
        while CustomUser.objects.filter(slug=random_slug).exists():
            random_slug = slugify(
                self.first_name + self.last_name + utils.generate_random_id())
        return random_slug

    def save(self, *args, **kwargs):
        """
        Performs some logic and;
        checks if a slug exists, if not, it creates one
        Then its finally save
        """
        if not self.slug:
            self.slug = self.generate_random_slug()
        super().save(*args, **kwargs)
