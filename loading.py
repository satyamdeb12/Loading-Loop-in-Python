#!/usr/bin/env python3
from os import system,name
from time import sleep

a = chr(47)
b = chr(45)
c = chr(92)

def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')
while True:
    print("{}  LOADING".format(a))
    sleep(0.2)
    clear()
    print("{}  LOADING".format(b))
    sleep(0.2)
    clear()
    print("{}  LOADING".format(c))
    sleep(0.2)
    clear()
