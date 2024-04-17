from django.urls import path
from .views import CallDataAPIView

urlpatterns = [
    path('call_data/', CallDataAPIView.as_view(), name='call-data')
]
