from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings

class Record(models.Model):
    created_at = models.DateTimeField(_("publication date"))
    phone_num = models.CharField(max_length=100)
    customer_num = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    plan = models.CharField(max_length=100, null=True)

    def __str__(self):
        return(f"{self.phone_num}")