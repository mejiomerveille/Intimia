from django.urls import path

from chats.consumers import *


websocket_urlpatterns = [
    path('ws/<int:id>/', PersonalChatConsumer.as_asgi()),
    path('ws/online/', OnlineStatusConsumer.as_asgi()),
    path('ws/notify/', NotificationConsumer.as_asgi())
]


    # path('ws/chat/<str:room_name>/',PersonalChatConsumer.as_asgi()),