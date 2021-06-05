from django.db import models
from listings.models import Listing


class Contact(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200,null=True)
    message = models.TextField()
    contact_date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(default=0)

    class Meta:
        ordering = ('-contact_date',)

    def __str__(self):
        return self.name
