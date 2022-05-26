from django.db import models
from django.shortcuts import reverse


class Cities(models.Model):
    name = models.CharField(max_length=150)
    date_pub = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_pub']

    def __str__(self):
        return self.name

    def get_delete_url(self):
        return reverse('delete_city_url', kwargs={'name': self.name})