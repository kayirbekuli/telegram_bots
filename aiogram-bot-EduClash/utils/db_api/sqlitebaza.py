import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):  # Sqlitega ati beremis
        self.path_to_db = path_to_db

    # db ga jalganatin func
    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    # Sql commandalarin ushin func
    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection  # DB ga jalg'aniw
        connection.set_trace_callback(logger)  # loggerlardi oxip atirmiz
        cursor = connection.cursor()  # cursor jaratip aldiq
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            name varchar(255) NOT NULL,
            klass varchar(255),
            phonenum varchar(13),
            PRIMARY KEY (id)
            );
"""  # PRIMARY KEY (id)  ozgeshe id basqa tablica mn jalg'a'gan kezde
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, klass: str = None, phonenum: str = ''):
        phonenum = phonenum.lstrip("+")  # + belgini olib tashlaymiz

        # Foydalanuvchi mavjudligini tekshiramiz
        if self.select_user(id=id):
            # Agar foydalanuvchi mavjud bo'lsa, uni yangilaymiz
            self.update_user_klass(klass, id)
            self.update_user_phone(phonenum, id)
        else:
            # Agar foydalanuvchi mavjud bo'lmasa, yangi qo'shamiz
            sql = """
            INSERT INTO Users(id, Name, klass, phonenum) VALUES(?, ?, ?, ?)
            """
            self.execute(sql, parameters=(id, name, klass, phonenum), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_klass(self, klass, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET klass=? WHERE id=?
        """
        return self.execute(sql, parameters=(klass, id), commit=True)

    def update_user_name(self, name, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET name=? WHERE id=?
        """
        return self.execute(sql, parameters=(name, id), commit=True)

    def update_user_phone(self, phonenum, id):
        phonenum = phonenum.lstrip("+")  # + belgini olib tashlaymiz
        sql = """
        UPDATE Users SET phonenum=? WHERE id=?
        """
        return self.execute(sql, parameters=(phonenum, id), commit=True)

    def get_user_ids(self):
        sql = "SELECT id FROM Users"
        return [row[0] for row in self.execute(sql, fetchall=True)]

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")