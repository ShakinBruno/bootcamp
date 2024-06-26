from django.core.asgi import get_asgi_application
from django.urls import re_path

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from bootcamp.messager.consumers import MessagerConsumer
from bootcamp.notifications.consumers import NotificationsConsumer

# from bootcamp.notifications.routing import notifications_urlpatterns
# from bootcamp.messager.routing import messager_urlpatterns

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    [
                        re_path(r"^notifications/$", NotificationsConsumer),
                        re_path(r"^(?P<username>[^/]+)/$", MessagerConsumer),
                    ]
                )
            )
        )
    }
)
