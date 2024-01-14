from rest_framework import viewsets
from .models import CustomerQuery
from .serializers import CustomerQuerySerializer

class CustomerQueryViewSet(viewsets.ModelViewSet):
    queryset = CustomerQuery.objects.all()
    serializer_class = CustomerQuerySerializer
