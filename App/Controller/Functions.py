import hashlib


class Functions:
    def __init__(self):
        pass

    def seprator(self, text):
        splited = text.split(' ', 1)
        if splited[0] == '':
            return False
        if len(splited) != 2 or splited[1] == '':
            return False
        return splited

    def make_md5(self, string):
        return hashlib.md5(string.encode('utf-8')).hexdigest()

    def student_code_check_length(self, code):
        if len(code) == 9:
            return True
        return False

    def check_is_command(self, string):
        if (string[0] == '!'):
            return True
        return False
