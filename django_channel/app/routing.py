from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/sc/', consumers.MySyncConsumer.as_asgi()),
    path('ws/async/', consumers.MyAsyncConsumer.as_asgi()),  # Async consumer
]