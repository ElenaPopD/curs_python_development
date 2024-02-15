from rest_framework.viewsets import ModelViewSet

from ..models import Produs, Producator

from .serializers import ProdusSerializer

class ProdusViewSet(ModelViewSet):
    queryset = Produs.objects.all()
    serializer_class = ProdusSerializer


class ProducatorViewSet(ModelViewSet):
    queryset = Producator.objects.all()
    serializer_class = ProdusSerializer

