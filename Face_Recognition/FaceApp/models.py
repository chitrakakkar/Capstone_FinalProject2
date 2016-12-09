from django.db import models

# Create your models here.


class Image_model(models.Model):
    image = models.ImageField(upload_to='images/')
    Saved_on = models.DateTimeField(auto_now_add=True)

class Analysed_model(models.Model):
    image = models.ImageField(upload_to='images/')
    Saved_on = models.DateTimeField(auto_now_add=True)


