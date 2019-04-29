from channels.routing import route

from chat.Consumers import ws_message

channel_routing = [
    route('websocket.receive' ws_message),
}
