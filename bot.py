import telebot as tl
from telethon.sync import TelegramClient
from telethon import functions, types
import time

client = TelegramClient("sesion", <api_id>, <api_hash>)
bot = tl.TeleBot(<token>)

client.start()

from_channel = <channel>
to_channel = <channel>

def main():
    channel_username = from_channel
    channel_entity=client.get_entity(channel_username)
    posts = client(functions.messages.GetHistoryRequest(
        peer=channel_entity,
        limit=100,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
    hash=0))
    return posts.messages[0]

last = main()   

while 1:
    time.sleep(5)
    now = main()
    print(last.id != main().id, last.id, main().id)
    if last.id != main().id:
        bot.send_message(to_channel, main().message)
    last = main()
    now = None