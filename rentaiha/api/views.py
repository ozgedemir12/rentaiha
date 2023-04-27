from rest_framework import viewsets
from rentaiha.api.serializer import IhaSerializer,CategorySerializer,BrandSerializer,ModelSerializer,IhaSerializerPost
from rest_framework.response import Response
from rentaiha.models import Iha,Category, Brand,Model


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


# RestFramework Iha modeli ile ilişkili bir API görünüm kümesi 
class IhaViewSet(viewsets.ModelViewSet):
    queryset = Iha.objects.all()
    serializer_class = IhaSerializer

    # kategori, marka veya model filtresine göre filtrelenmiş öğeleri döndürür.
    def list(self, request):
        print(request.GET.get('category'))
        if request.GET.get('category') is not None:
            queryset = Iha.objects.filter(category__name=request.GET.get('category'))
            serializer = IhaSerializer(queryset, many=True)
            return Response(serializer.data)
        
        elif request.GET.get('brand') is not None:
            queryset = Iha.objects.filter(brand__name=request.GET.get('brand'))
            serializer = IhaSerializer(queryset, many=True)
            return Response(serializer.data)
        
        elif request.GET.get('model') is not None:
            queryset = Iha.objects.filter(model__name=request.GET.get('model'))
            serializer = IhaSerializer(queryset, many=True)
            return Response(serializer.data)
        
        else:
            queryset = Iha.objects.all()
            serializer = IhaSerializer(queryset, many=True)
            return Response(serializer.data)
        



    #create func.
    def create(self, request, *args, **kwargs):
        serializer = IhaSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response(serializer.data)
    

    #update func.
    def update(self, request, pk, *args, **kwargs):
        instance = Iha.objects.get(pk=pk)
        serializer = IhaSerializerPost(instance, data=request.data, partial=True) #sadece değişen alanların güncellenmesi için partial=True verdik

        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response(serializer.data)


    
   

    