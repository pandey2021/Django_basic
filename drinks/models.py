from django.db import models

class Drinks(models.Model):
    name = models.CharField(max_length= 200)
    desc = models.CharField(max_length= 500)

    def __str__(slef):
        return slef.name