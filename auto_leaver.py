#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *
from random import sample

import time
import requests

client = Client("user", "pass")
thread_id = "3202204843184747"
thread_type = ThreadType.GROUP

print("Own id: {}".format(client.uid))

while True:
    try:
        r = requests.get("https://inspirobot.me/api?generate=true")
        client.sendRemoteImage(r.text, Message(text="Here's your motivational quote for today:"), thread_id=thread_id, thread_type=thread_type)
        time.sleep(86400)
    except:
        print("Error something went wrong")
        time.sleep(86400)
client.logout()
