from django.contrib import admin 

from .models import Iha 

class IhaAdmin(admin.ModelAdmin):
  list_display = ("brand", "model", "weight","category")

admin.site.register(Iha , IhaAdmin)
