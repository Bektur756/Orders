# views.py

import csv
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import OrderHistory
from .serializers import OrderHistoryListSerializer, OrderHistorySerializer


class OrderHistoryListAPIView(ListAPIView):
    queryset = OrderHistory.objects.all()[:5]
    serializer_class = OrderHistoryListSerializer


class OrderHistoryCreateAPIView(CreateAPIView):
    queryset = OrderHistory.objects.all()
    serializer_class = OrderHistorySerializer

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')

        if file and file.name.endswith('.csv'):
            csv_file = file.read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                serializer = OrderHistorySerializer(data={
                    'customer': row['customer'],
                    'item': row['item'],
                    'total': row['total'],
                    'quantity': row['quantity'],
                    'date': row['date']
                })
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response("Data uploaded successfully", status=status.HTTP_201_CREATED)
        else:
            return Response("Invalid file format. Please upload a CSV file.", status=status.HTTP_400_BAD_REQUEST)