"""import sqlite3
class Database:
    def __init__(self):
        self.conn=sqlite3.connect("database.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXIST users(id INTEGER PRIMARY KEY, first_name TEXT last_name TEXT password optional[str]")
        self.conn.commit()
        
    def fetch(self,id):
        self.cur.execute("SELECT password FROM users WHERE id=?,(id,)")
        rows = self.cur.fetchall()
        return rows
    
    def insert (self, first_name, last_name,password):
        self.cur.execute("INSERT INTO users VALUES(NULL,?, ?, ?)", (first_name,last_name,password))
        self.conn.commit()
        
    def remove(self,id):
        self.cur.execute("DELETE FROM users WHERE id=?", (id,))
        self.conn.commit()
        
    def update(self, id, first_name, last_name, password):
        self.conn.execute("UPDATE users SET first_name =?, last_name=?, password=?, WHERE id= ?",(first_name, last_name,password))
        self.conn.commit()
        
    def __del__(self):    
        self.conn.close()"""
        
import sqlite3

conn=sqlite3.connect("majaribio.db")
cursor = conn.cursor()
cursor=conn.close()

command1= """ CREATE TABLE IF NOT EXISTS stores (id INTERGER PRIMARY KEY, name TEXT)"""
cursor.execute(command1)