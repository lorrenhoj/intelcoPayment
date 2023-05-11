from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    phone_num = models.CharField(max_length=50)
    customer_num = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.phone_num} {self.customer_num}")