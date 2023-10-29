from django.urls import path
from api_v1.views import ProductListAPIView, ProductCreateAPIView


urlpatterns = [
    path('list/', ProductListAPIView.as_view(), name='list_products'),
    path('upload/', ProductCreateAPIView.as_view(), name='excel-upload'),
]
