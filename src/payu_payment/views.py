from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import LogPurchase
from .serializers import LogPurchaseSerializer

class LogList(ListAPIView):
    queryset = LogPurchase.objects.all()
    serializer_class = LogPurchaseSerializer

class CreateLog(CreateAPIView):
    
    serializer_class = LogPurchaseSerializer
    queryset = LogPurchase.objects.all()

    def create(self, request, *args, **kwargs):

        risk = request.data["risk"]
        customer_number = request.data["customer_number"]
        request.data["date"] = request.data["date"].replace('.','-')
        if not risk:
            request.data["risk"] = 0
        
        if not customer_number:
            request.data["customer_number"] = 0

        print("data:", request.data)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
        