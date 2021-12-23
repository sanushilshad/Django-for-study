from django.http import HttpResponse
from channels.handler import AsgiHandler

from channels import Group


def ws_connect(message):
    Group('users').add(message.reply_channel)


def ws_disconnect(message):
    Group('users').discard(message.reply_channel)  