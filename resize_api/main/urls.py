from django.urls import path

from .views import *
from .serializers import *

app_name = 'main'
urlpatterns = [
    path('<int:pk>/', ResizeDetailView.as_view(), name='resize_detail'),
    path('', ResizeCreateView.as_view(), name='resize'),
]