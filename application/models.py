import ast
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Sensor(models.Model):
    name = models.CharField(max_length=50, blank=False)
    kind = models.CharField(max_length=50, blank=True)
    values = models.CharField(max_length=128, blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'pk': self.pk
        }
        return reverse('app:detail', kwargs=kwargs)
