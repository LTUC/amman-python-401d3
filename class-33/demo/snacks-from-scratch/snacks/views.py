from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Snack
from .serializers import SnackSerializer

class SnackListCreate(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
