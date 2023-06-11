from django.db import models
from django.utils import timezone

# Create your models here.


class Contact(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=100, blank=True)
  phone = models.CharField(max_length=50)
  email = models.EmailField(max_length=150, blank=True)
  description = models.TextField(blank=True)
  created_at = models.DateTimeField(default=timezone.now)

  def __str__(self) -> str:
    return f'{self.first_name} {self.last_name}'
