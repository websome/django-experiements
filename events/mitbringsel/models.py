from django.db import models

class Mitbringsel(models.Model):
    type = models.CharField(max_length=200)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text



