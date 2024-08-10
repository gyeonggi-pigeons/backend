from django.contrib import admin
from .models import Nutrient, ImageResponseCache
# Register your models here.
admin.site.register(Nutrient)
admin.site.register(ImageResponseCache)
