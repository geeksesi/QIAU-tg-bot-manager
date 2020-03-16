import asyncio
from telethon import TelegramClient, events, sync, functions
from App.Controller.Controller import Controller
from telethon.tl.functions.channels import JoinChannelRequest
from EnvParser import EnvParser

envs = EnvParser()

api_id = envs.get_env("api_id")
api_hash = envs.get_env("api_hash")
admins = envs.get_env("admins")
client_name = envs.get_env("client_name")
client = TelegramClient(client_name, api_id, api_hash)
app = Controller(envs.get_env("db_name"))
loop = asyncio.get_event_loop()


async def cron_job():
    me = await client.get_me()
    dialogs = await client.get_dialogs()
    for d in dialogs:
        if d.id == -1001377564387:
            channel = d
            while True:
                await app.group_check(channel, client, me.id, admins)
                await asyncio.sleep(60)


async def main():
    await cron_job()


@client.on(events.NewMessage)
async def my_event_handler(event):
    await event.message.mark_read()
    if event.chat_id == -1001166405576:
        return
    if event.from_id in admins:
        admin_answer = app.admin_job(event.raw_text)
        await event.reply(admin_answer)
        return

    check_code = app.do_job(event.raw_text, event.from_id)

    if check_code == "code 1":
        await event.reply(
            'سلام. لطفا شماره دانشجویی خودتون رو برای عضویت در کانال وارد کنید'
        )
    elif check_code == "code 2":
        await event.reply(
            "سلام \n لطفا شماره دانشجویی خود را برای عضویت در کانال دروس با اعداد انگلیسی وارد کنید.. \n با تشکر"
        )
    elif check_code == "code 3":
        await event.reply(
            'سلام\n یک‌ نفر قبلا با شماره دانشجویی شما وارد کانال شده است. در صورت بروز مشکل با مدیر گروه رشته خود از طریق ایمیل تماس حاصل فرمایید. \n  با تشکر.'
        )
    elif check_code == False:
        await event.reply(
            'متاسفانه مشکلی پیش‌ آمده است. از طریق ایمیل با مدیرگروه رشته خود تماس گرفته و مشکل را گزارش کنید.'
        )
    else:
        text = ""
        if check_code == "p":
            text = "دانشجوی رشته مهندسی کامپیوتر خوش آمدید "
        elif check_code == "b":
            text = "دانشجوی رشته مهندسی برق  خوش آمدید "
        elif check_code == "n":
            text = "دانشجوی رشته مهندسی کامپیوتر (ناپیوسته) خوش آمدید "
        else:
            await event.reply('مشکلی پیش‌ آمده با مدیرگروه تماس بگیرید.')
            return False
        await event.reply(
            text +
            '\n در کانال دروس تخصصی مهندسی کامپیوتر و برق با لینک زیر عضو شوید.  \n https://t.me/joinchat/AAAAAFIb9uO8S4lGQLct-g'
        )


with client:
    client.loop.run_until_complete(main())

client.start()
client.run_until_disconnected()
