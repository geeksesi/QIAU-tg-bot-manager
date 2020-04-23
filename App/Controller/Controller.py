from App.Model.Model import Model
from App.Controller.Admin import Admin
from App.Controller.Functions import Functions


class Controller:
    def __init__(self, db_name):
        self.model = Model(db_name)
        self.functions = Functions()
        self.admin = Admin(self.model, self.functions)

    def do_job(self, string, chat_id):
        if not self.functions.student_code_check_length(string):
            return "code 1"
        code = self.functions.make_md5(string)
        student_type = self.model.check_code(code)
        if not student_type:
            return "code 2"
        check_duplicate = self.model.check_accept(code)
        if check_duplicate != True and str(check_duplicate) != str(chat_id):
            return "code 3"
        if str(check_duplicate) == str(chat_id):
            return student_type
        if not self.model.new_accept(code, student_type, chat_id):
            return False
        return student_type

    async def group_check(self, channel, client, me_id, admins):
        print("i'm here")
        my_channel = await client.get_participants(channel)
        for user in my_channel:
            # print(user.is_admin)
            if user.id in admins:
                continue
            if user.id == me_id:
                continue
            if user.bot:
                continue
            if (not self.model.check_accept_chat_id(user.id)):
                # print(user.id, user.first_name, user.last_name, user.username)
                await self.kick_from_channel(client, channel, user)

    async def kick_from_channel(self, client, channel, user):
        try:
            print(f"{user.first_name} Was kicked from channel")
            await client.kick_participant(channel, user)
        except ProcessLookupError:
            print("nothing")

    def admin_event(self, event):
        return self.admin.event_handle(event)
