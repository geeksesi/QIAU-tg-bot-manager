class Admin:
    """ this class will manage admin methodes in bot.
    
    Returns:
        None
    """
    def __init__(self, model, functions):
        """[summary]
        
        Arguments:
            model {[type]} -- [description]
            functions {[type]} -- [description]
        """
        self.model = model
        self.functions = functions

    def event_handle(self, event):
        """ admin private message event handle
        
        Arguments:
            event {[type]} -- telethon new message event
        
        Returns:
            int -- message code :
                - 101 : Help message
                - 104 : invalid input
        """
        text = event.raw_text
        if self.functions.check_is_command(text):
            if text == "!help":
                return 101
            return 104

        explode = self.functions.seprator(event.raw_text)
        if not explode:
            return 104
        if explode[0] == "reset_code":
            answer = self.reset_user_chat_id(explode[1])
            return answer

    def reset_user_chat_id(self, code):
        """[summary]
        
        Arguments:
            code {[type]} -- [description]
        
        Returns:
            int -- message code :
                - 112 : code is invalid
                - 111 : success
                - 113 : database error
        """
        if not self.functions.student_code_check_length(code):
            return 112
        code_md5 = self.functions.make_md5(code)
        delete_status = self.model.reset_user_chat_id(code_md5)
        if delete_status:
            return 111
        return 113