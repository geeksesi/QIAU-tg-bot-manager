from telethon import TelegramClient, events, sync, functions
from App.Controller.Bot import Bot
from telethon.tl.functions.channels import JoinChannelRequest
from EnvParser import EnvParser

envs = EnvParser()
api_id = envs.get_env("api_id")
api_hash = envs.get_env("api_hash")
admins = envs.get_env("admins")
db_name = envs.get_env("db_name")
client_name = envs.get_env("client_name")
client = TelegramClient(client_name, api_id, api_hash)
client = TelegramClient(client_name, api_id, api_hash)

bot = Bot(client, admins, db_name)


@client.on(events.NewMessage(incoming=True))
async def message_event(event):
    print(event.raw_text)
    await bot.my_event_handler(event)


# with client:
#     client.loop.run_until_complete(bot.cron_job())

client.start()
client.run_until_disconnected()
