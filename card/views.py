from rest_framework import viewsets
from .models import Card, Service
from .serializers import CardSerializer, ServiceSerializer
from .permissions import IsOwnerOrAdmin

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsOwnerOrAdmin]
    
    
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsOwnerOrAdmin]
