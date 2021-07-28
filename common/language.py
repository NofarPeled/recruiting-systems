from django.db import models
from django.utils.translation import gettext_lazy as _

class Languages(models.TextChoices):
    EN = 'en', _('English')
    HE = 'he', _('Hebrew')


# how to use the language model: 
# language = models.CharField(max_length=2, choices=Languages.choices, default=Languages.EN)
