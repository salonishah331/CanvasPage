from django.db import models



class Canvas(models.Model):
    canvas = models.TextField(blank = True, null = False)


    def __str__(self):
        return self.text

# Create your models here.
