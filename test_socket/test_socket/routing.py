from location import consumers
channel_routing = {
    'websocket.connect': consumers.ws_connect,
    'websocket.disconnect': consumers.ws_disconnect,
}