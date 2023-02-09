import psycopg2
import os
from datetime import date
import datetime


#url = os.environ['DATABASE_URL']
url = "postgresql://database:AVNS_A_1U7iHgpNTlBTiivCe@app-4c8a87f2-73ff-4c8a-9ca0-e9888e28550b-do-user-13531893-0.b.db.ondigitalocean.com:25060/database?sslmode=require"

def add_user(id):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""INSERT INTO users(id) VALUES (%s);""", (id,))
    conn.close()
    cur.close()
    return True

def enable_premium(id, date):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""UPDATE users SET date = %s WHERE id = %s""", (date, id))
    conn.close()
    cur.close()
    return True

def disable_premium(id):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""UPDATE users SET date = %s WHERE id = %s""", (None, id))
    conn.close()
    cur.close()
    return True

def get_info(id):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""SELECT * FROM users WHERE id = %s""", (id,))
    r = cur.fetchone()
    conn.close()
    cur.close()
    return r

def change_wordType(id, value):
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""UPDATE users SET wordType = %s WHERE id = %s""", (value, id))
    conn.close()
    cur.close()
    return True

def get_users_list():
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""SELECT name from users;""")
    r = []
    for tuple in cur.fetchall():
        r.append(tuple[0])
    conn.close()
    cur.close()
    return r

def get_ids():
    conn = psycopg2.connect(url, sslmode="require")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""SELECT id from users;""")
    r = []
    for tuple in cur.fetchall():
        r.append(tuple[0])
    conn.close()
    cur.close()
    return r

#enable_premium(852988643, "2022-10-11")
