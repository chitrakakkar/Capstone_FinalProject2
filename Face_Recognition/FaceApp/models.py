from django.db import models

# Create your models here.


class Image_model(models.Model):
    image = models.CharField(max_length=300, null=False)
    Saved_on = models.DateTimeField(null=False, auto_now=True)