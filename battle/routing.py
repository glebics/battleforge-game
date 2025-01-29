from django.urls import path
from battle.consumers import BattleConsumer

websocket_urlpatterns = [
    path("ws/battle/<str:battle_id>/", BattleConsumer.as_asgi()),
]
