import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.db import connection


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user_id = self.scope["user"].id

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT name, surname FROM myprofile_profile  WHERE user_id = %s",
                [user_id])
            row = cursor.fetchone()

            if row is not None:
                name, surname_name = row
                # Дальнейшая обработка полученных данных
            else:
                # Обработка случая, если запись не найдена
                name = "инкогнитов"
                surname_name = "аноним"

        message = f'{name} {surname_name}: {text_data_json["message"]}'

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
