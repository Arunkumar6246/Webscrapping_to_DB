import psycopg2 as pg


def create():
    conn=pg.connect(" dbname='db_name' user='postgres' password='Admin' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute(" CREATE TABLE IF NOT EXISTS rawdata ( Title TEXT,Ad_by TEXT,offers TEXT,rate TEXT,per_sqft INTEGER ) ")
    conn.commit()
    conn.close()

def insert(Title,Ad_by,offers,rate,per_sqft):
    conn=pg.connect(" dbname='real_estate' user='postgres' password='Admin' host='localhost' port=5432 ")
    cur=conn.cursor()
    cur.execute("INSERT INTO RAWDATA (Title,Ad_by,offers,rate,per_sqft) VALUES(%s,%s,%s,%s,%s)",(Title,Ad_by,offers,rate,per_sqft))
    conn.commit()
    conn.close()

create()
