import unicodedata
from sys import stdin

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

def string_shift(text:str, key:int):
    text = stdin.read()
    print(text)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").upper() # odstranění znaků s háčkem atd. 
    result = ""
    for char in text:
        if char >= "A" and char <= "Z":
            position = ord(char) - 65 
            new_position = (position + key) % 26
            result += chr(new_position + 65) 
        else:
            continue    
    return result
print(string_shift("Ahoj", 3)) 
