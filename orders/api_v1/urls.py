from django.urls import path
from api_v1.views import OrderHistoryListAPIView, OrderHistoryCreateAPIView


urlpatterns = [
    path('list/', OrderHistoryListAPIView.as_view(), name='order-history-list'),
    path('upload/', OrderHistoryCreateAPIView.as_view(), name='excel-upload'),
]
