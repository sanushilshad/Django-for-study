from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
import time
import json
import urlparse

def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    json_data = json.loads(message.content['text'])
    user = json_data['user']
    start_time = json_data['start_time']
    end_time = json_data['end_time']
    date = json_data['date']
    group_name = '{}-{}-{}-{}'.format(user, date, start_time, end_time)
    Group(group_name).send({
        "text": user,
    })

def ws_connect(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    json_data = urlparse.parse_qs(message.content['query_string'])
    user = json_data['user'][0]
    date = json_data['date'][0]
    start_time = json_data['start_time'][0]
    end_time = json_data['end_time'][0]
    group_name = '{}-{}-{}-{}'.format(user, date, start_time, end_time)
    Group(group_name).add(message.reply_channel)

        
