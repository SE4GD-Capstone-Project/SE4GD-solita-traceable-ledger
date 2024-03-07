from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from NodeAPI import views
router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('products/', views.demo_get),
    path('', include(router.urls)),
]
