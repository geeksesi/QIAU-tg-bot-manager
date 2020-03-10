import sqlite3


class Model:
    def __init__(self):
        self.db = sqlite3.connect('QIAU_CEIT.sql')

    def check_code(self, code):
        c = self.db.cursor()
        query = "SELECT * FROM all_students WHERE code='%s'" % str(code)
        c.execute(query)
        result = c.fetchall()
        c.close()
        if not result:
            return False
        return result[0][2]

    def new_accept(self, code, user_type, chat_id):
        c = self.db.cursor()
        last_id_query = "select max(id) from accepted"
        c.execute(last_id_query)
        last_id_result = c.fetchone()
        last_id = 0
        if last_id_result[0] != None:
            last_id = last_id_result[0]
        #
        insert_query = "INSERT INTO accepted (id, code, type, chat_id) VALUES (?, ?, ?, ?);"
        query_data = ((last_id + 1), str(code), str(user_type), str(chat_id))
        c.execute(insert_query, query_data)
        self.db.commit()
        c.close()
        return True

    def check_accept(self, code):
        c = self.db.cursor()
        check_query = "SELECT * FROM accepted WHERE code='%s'" % str(code)
        c.execute(check_query)
        check_result = c.fetchall()
        c.close()
        if check_result:
            return check_result[0][3]
        return True

    def check_accept_chat_id(self, chat_id):
        c = self.db.cursor()
        check_query = "SELECT * FROM accepted WHERE chat_id='%s'" % str(
            chat_id)
        c.execute(check_query)
        check_result = c.fetchall()
        c.close()
        if check_result:
            return True
        return False
