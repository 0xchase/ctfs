#!/usr/bin/python3

from unidecode import unidecode

chars = ""
with open("speed_demon.rb", "r") as f:
    chars = f.read()

for i in range(0, len(chars)):
    if chars[i] == "\\" and chars[i+1] == "u" :
        #print(unidecode(chars[i:i+4])
        print("")
        print(chars[i:i+4])
        print("")
        i += 4
    else:
        print(chars[i], end='')
