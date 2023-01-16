import base64
import os
import random
import codecs

from models.index_model import get_cars, set_image_to_car
from utils import get_db_connection

def getRandomFile(path):
    return random.choice(os.listdir(path))

conn = get_db_connection()

f_damp = open('carsdb.db','r', encoding ='utf-8-sig')
damp = f_damp.read()
f_damp.close()

conn.executescript(damp)
conn.commit()

df_cars = get_cars(conn)

for i in range(1, len(df_cars) + 1):
    dir = os.path.dirname(os.path.abspath(__file__)) + "\static\damp"
    fileName = getRandomFile(dir)
    file = open(dir + chr(92) + fileName, "rb")
    base64img = base64.standard_b64encode(file.read()).decode()
    set_image_to_car(conn, i, base64img)

conn.close()

