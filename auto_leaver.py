#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *
from random import sample

import time

client = Client("user", "pass")
thread_id = "3202204843184747" #add the thread id (messenger.com on the URL)
thread_type = ThreadType.GROUP

print("Own id: {}".format(client.uid))

client.send(Message(text="Hi me!"), thread_id=client.uid, thread_type=ThreadType.USER)
solv = ["ToodeBOT on hetkel "]
insp2 = ["Seek success, but prepare for vegetables.", "If you are the only one who matters in the afterlife, you will rule the afterlife.",
"Before sex, comes sex.", "Prepare for failure, yell and do not excpect anything.", "Before the inspiration, comes the slaughter.", "Keep panicking.",
"If you want to get somewhere in life you have to try to be dead.", "Hate the mountains", "Don't argue with success. be naked.", "Whenever you're dead, remember to never lie",
"New ideas have been invented to be destroyed bby ambitions.", "Wait for others to follow. Or don't", "Be a coward. Be humane. Be better.", "To inspire hunger means to inspire FIGHTERS.",
"Only when you learn to understand the full potential of lies, will you get the best.","Don't come", "There is a clear link between happiness and human sacrifice.",
"Simply being famous doesn't mean you are not loud.", "It's sick to ignore superiority.", "'Psychiatrist' actually means 'Hermaphrodite'","If you can drown him, you can tear yourself away from him.",
"Pursue what is polarizing, not what is realistic", "Very few people become mental patients because it sounded like a good idea at the time.",
"Embrace multiresistant bacteria. Recieve nature.", "Show fame. Lazy fame.", "Look Freaky", "The experience of being average can be a lot similar to being burned at a stake.", "My soul is perfect."]

insp = ["There are shitty people and there are not-so-shitty-people", "To some it's humanity but to some it's nothing more than just text",
"Memories are there to murder your economy", "Realize. Depression. Becomes. The. Grand. Master", "Art is 50% premotion and 50% idiocity", "Blood in the urine can be the universe telling you to have faith",
"If one expects a goal, it must prepare for art", "Ignore warnings, never ask questions"]

nr = [[i] for i in range(len(insp))]
u =  sample(nr,len(nr))
print(nr)
print(u)
n = 0
x = 0
asdf = 0
while True:
    try:
        if thread_type == ThreadType.GROUP:
            client.send(Message(text=u[x][0]), thread_id=client.uid, thread_type=ThreadType.USER)
        time.sleep(5)
    except:
        time.sleep(5)
client.logout()
