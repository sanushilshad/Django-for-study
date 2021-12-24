
from channels import route, route_class
from location.consumers import MyConsumer 

channel_routing = [
    route_class(MyConsumer, path=r"^/chat/"),
]
