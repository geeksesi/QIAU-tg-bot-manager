from App.Controller.Controller import Controller
import asyncio


class Bot:
    def __init__(self, client, admins, db_name):

        self.app = Controller(db_name)
        self.loop = asyncio.get_event_loop()
        self.admins = admins
        self.client = client

    async def cron_job(self):
        self.me = await self.client.get_me()
        # dialogs = await self.client.get_dialogs()
        # for d in dialogs:
        #     if d.id == -1001377564387:
        #         channel = d
        #         while True:
        #             await self.app.group_check(channel, self.client,
        #                                        self.me.id, self.admins)
        #             await asyncio.sleep(60)

    async def my_event_handler(self, event):
        await event.message.mark_read()
        if event.is_group == True:
            await self.group_message_handle(event)
        elif event.is_channel == True:
            await self.channel_message_handle(event)
        elif event.is_private == True:
            await self.private_message_handle(event)
        else:
            print("what happend ?")

        # check_code = self.app.do_job(event.raw_text, event.from_id)

        # if check_code == "code 1":
        #     await event.reply(
        #         'سلام. لطفا شماره دانشجویی خودتون رو برای عضویت در کانال وارد کنید'
        #     )
        # elif check_code == "code 2":
        #     await event.reply(
        #         "سلام \n لطفا شماره دانشجویی خود را برای عضویت در کانال دروس با اعداد انگلیسی وارد کنید.. \n با تشکر"
        #     )
        # elif check_code == "code 3":
        #     await event.reply(
        #         'سلام\n یک‌ نفر قبلا با شماره دانشجویی شما وارد کانال شده است. در صورت بروز مشکل با مدیر گروه رشته خود از طریق ایمیل تماس حاصل فرمایید. \n  با تشکر.'
        #     )
        # elif check_code == False:
        #     await event.reply(
        #         'متاسفانه مشکلی پیش‌ آمده است. از طریق ایمیل با مدیرگروه رشته خود تماس گرفته و مشکل را گزارش کنید.'
        #     )
        # else:
        #     text = ""
        #     if check_code == "p":
        #         text = "دانشجوی رشته مهندسی کامپیوتر خوش آمدید "
        #     elif check_code == "b":
        #         text = "دانشجوی رشته مهندسی برق  خوش آمدید "
        #     elif check_code == "n":
        #         text = "دانشجوی رشته مهندسی کامپیوتر (ناپیوسته) خوش آمدید "
        #     else:
        #         await event.reply('مشکلی پیش‌ آمده با مدیرگروه تماس بگیرید.')
        #         return False
        #     await event.reply(
        #         text +
        #         '\n در کانال دروس تخصصی مهندسی کامپیوتر و برق با لینک زیر عضو شوید.  \n https://t.me/joinchat/AAAAAFIb9uO8S4lGQLct-g'
        #     )

    async def channel_message_handle(self, event):
        return None

    async def group_message_handle(self, event):
        return None

    async def private_message_handle(self, event):
        if event.chat_id in self.admins:
            await self.admin_message_handle(event)
            return None

    async def admin_message_handle(self, event):
        admin_answer = self.app.admin_event(event)
        print(admin_answer)
        await event.reply(str(admin_answer))
