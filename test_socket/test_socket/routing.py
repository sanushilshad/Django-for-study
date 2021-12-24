from channels.routing import route
from location.consumers import ws_message, ws_connect

channel_routing = [
    route("websocket.receive", ws_message),
    route("websocket.connect", ws_connect),
]