from django.contrib import admin 
from .models import Iha,Brand,Category,Model

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display=('name',)
  class Meta:
    model=Category


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
  list_display=('name',)
  class Meta:
    model=Model

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
  list_display=('id','name',)
  class Meta:
    model=Brand


class IhaAdmin(admin.ModelAdmin):
  list_display = ("brand", "model", "weight","category")
  class Meta:
    model=Iha


admin.site.register(Iha , IhaAdmin)
