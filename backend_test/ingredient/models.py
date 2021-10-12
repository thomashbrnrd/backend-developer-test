from django.db import models
from django.utils.translation import gettext_lazy as _

from . import choices


class Ingredient(models.Model):
    name = models.CharField(_("Ingredient"), max_length=250)

    category = models.CharField(choices=choices.CATEGORIES, max_length=64)

    unit = models.CharField(choices=choices.UNITS, max_length=64)

    cost_per_unit = models.FloatField(_("Cost Per Unit"), null=True, blank=True)

    is_available = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
