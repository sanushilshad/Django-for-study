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
    group_name = clean_query_string('{}-{}-{}-{}'.format(user, date, start_time, end_time))
    Group(group_name).send({
        "text": user,
    })

def ws_connect(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    json_data = urlparse.parse_qs(message.content['query_string'])
    user = json_data['user']
    date = json_data['date']
    start_time = json_data['start_time']
    end_time = json_data['end_time']
    group_name = clean_query_string('{}-{}-{}-{}'.format(user, date, start_time, end_time))
    Group(group_name).add(message.reply_channel)

def clean_query_string(query_string):
    query_string = query_string.replace('[', '')
    query_string = query_string.replace(']', '')
    query_string = query_string.replace("'", '')
    query_string = query_string.replace('"', '')
    return query_string
        
