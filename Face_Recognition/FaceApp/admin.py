from django.contrib import admin
from .models import Image_model, Analysed_model

# Register your models here.
admin.site.register(Image_model)
admin.site.register(Analysed_model)