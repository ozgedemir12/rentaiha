from rest_framework import serializers

from rentaiha.models import Iha,Category,Model,Brand

class CategorySerializer(serializers.ModelSerializer):
     class Meta:
          model=Category
          fields=('name','id')

    
class ModelSerializer(serializers.ModelSerializer):
     class Meta:
          model=Model
          fields=('name','id')

class BrandSerializer(serializers.ModelSerializer):
     class Meta:
          model=Brand
          fields=('name','id')


class IhaSerializer(serializers.ModelSerializer):
    category=CategorySerializer()# ilişkisel tablonun içeriğini alır. Inner.join
    brand=BrandSerializer() # ilişkisel tablonun içeriğini alır. Inner.join
    model=ModelSerializer()   # ilişkisel tablonun içeriğini alır. Inner.join
    class Meta:
         model = Iha
         fields = ('id','brand' , 'model', 'category', 'weight', 'img')


class IhaSerializerPost(serializers.ModelSerializer):
    class Meta:
         model = Iha
         fields = ('id','brand' , 'model', 'category', 'weight', 'img')


