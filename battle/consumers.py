import json
from channels.generic.websocket import AsyncWebsocketConsumer


class BattleConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.battle_id = self.scope['url_route']['kwargs']['battle_id']
        self.group_name = f"battle_{self.battle_id}"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'battle_message',
                'message': data
            }
        )

    async def battle_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))
