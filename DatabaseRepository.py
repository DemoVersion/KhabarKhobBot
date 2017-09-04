import sqlite3
class DatabaseRepository(object):
    """A Simple Class for KhabarKhobBot for Connecting to the SQLite Database

    Attributes:
        conn: connection.
        c: curser.
    """
    def __init__(self, path):
        """Return a DatabaseRepository object. """
        self.conn = sqlite3.connect(path);
        self.c = self.conn.cursor()

    def get_all_userid(self,time):
        arr_t = (time,)
        self.c.execute('SELECT * FROM users WHERE users.time=?', arr_t)
        return self.c.fetchall()

    def insert_new_user(self,user_id,time): 
        arr_users = (user_id,time)
        self.c.execute('INSERT INTO users VALUES (?,?)', arr_users)
        self.conn.commit()

    def close(self):
    	self.conn.close()
