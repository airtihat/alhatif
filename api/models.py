from django.db import models

class APILog(models.Model):
    endpoint = models.CharField(max_length=255)
    request_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.endpoint
