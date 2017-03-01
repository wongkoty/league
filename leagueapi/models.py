from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from django.db import models

# Create your models here.

class Champion(models.Model):
    
    name = models.CharField(default='', max_length=120)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name

