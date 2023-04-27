from django.urls import path,include
from . import views
from .api.views import IhaViewSet,CategoryViewSet,BrandViewSet,ModelViewSet
from rest_framework import routers

#RestFramework Routers
router = routers.DefaultRouter()
router.register(r'deneme',IhaViewSet,basename='Iha')
router.register(r'model',ModelViewSet,basename='Model')
router.register(r'brand',BrandViewSet,basename='Brand')
router.register(r'category',CategoryViewSet,basename='Category')
app_name="rentaiha"

urlpatterns = [

    # path('myadmin/', views.add_iha, name='add_iha'),
    path('api/', include(router.urls)),
    path('', views.search_iha, name='index'),
    path('myadmin/', views.admin_iha, name='myadmin'),
    path('update/<int:id>/', views.update_iha, name='update'),
    path('home/', views.add_iha, name='home'),
    path('login/', views.LoginPage, name='login'),
    path('register/', views.SignupPage, name='register'),
]