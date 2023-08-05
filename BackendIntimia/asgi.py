"""
ASGI config for BackendIntimia project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BackendIntimia.settings')

# application = get_asgi_application()


# mysite/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from chats.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BackendIntimia.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()
from django.urls import path

from chats.consumers import *

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        'websocket': AuthMiddlewareStack(URLRouter([
            path('ws/<int:id>/', PersonalChatConsumer.as_asgi()),
            path('ws/online/', OnlineStatusConsumer.as_asgi()),
            path('ws/notify/', NotificationConsumer.as_asgi())
        ]))
    }
)