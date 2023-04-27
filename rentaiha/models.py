from django.db import models

#Brand Model
class Brand(models.Model):
    name=models.CharField(max_length=100)
    id=models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.name}"
    
#Model Model
class Model(models.Model):
    name=models.CharField(max_length=100,verbose_name='Model Adı')
    id=models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.name}"


#Kategori Model
class Category(models.Model):
    name=models.CharField(max_length=100)
    id=models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.name}"
    
#Relationship Model
class Iha(models.Model):
    brand=models.ForeignKey(Brand,verbose_name='Brand',on_delete=models.CASCADE)
    model=models.ForeignKey(Model,verbose_name='Model',on_delete=models.CASCADE)
    weight=models.IntegerField(null= True, blank=True)
    category=models.ForeignKey(Category,verbose_name='Category',on_delete=models.CASCADE)
    img=models.ImageField(null= True, blank=True)
  
