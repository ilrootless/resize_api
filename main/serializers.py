from rest_framework import serializers

from .models import Resize


class ResizeDetailSerializer(serializers.ModelSerializer):
    '''Данные операции'''

    class Meta:
        model = Resize
        fields = '__all__'

class ResizeCreateSerializer(serializers.ModelSerializer):
    '''Добавление запроса'''

    class Meta:
        model = Resize
        exclude = ('result',)
