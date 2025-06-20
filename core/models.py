from django.db import models

class UserProfile(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name
