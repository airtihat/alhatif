from django.db import models

class AdCampaign(models.Model):
    title = models.CharField(max_length=200)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
