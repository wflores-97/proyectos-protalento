import readchar
key = readchar.readkey
from readchar import readkey, key

while True:
    up = readkey()
    if up == key.UP:
        print("juego finalizado")
        break