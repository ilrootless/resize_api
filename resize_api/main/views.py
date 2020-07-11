from rest_framework import generics

from .serializers import *
from .tasks import resize_image


class ResizeDetailView(generics.RetrieveAPIView):
    '''Вывод деталей операции'''
    queryset = Resize.objects.all()
    serializer_class = ResizeDetailSerializer

class ResizeCreateView(generics.CreateAPIView):
    '''Добавление запроса на ресайз'''
    serializer_class = ResizeCreateSerializer

    def perform_create(self, serializer):
        pk = serializer.save().id
        resize_image.delay(pk)
