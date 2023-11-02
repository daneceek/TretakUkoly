import unicodedata
import string
from sys import stdin, path
import click

@click.command()
@click.option("--method", "-m", help = "Vyberte metodu | encode nebo decode", type = str)
@click.option("--files", "-f",  nargs = 2, default =["-"],  help = "Zadejte cestu k souboru, který chcete dekódovat nebo enkódovat a jako druhý argument cestu k výstupu | pomlčka spustí stdin")

def main(method, files):
    input, output = files
    if method == "encode":
        # folder_opening(input, output, shift)
        pass
    elif method == "decode":
         # folder_opening(input, output, shift)
        pass
def folder_opening(input, output, shift):
    with open(input, "r") as input:
            text = caesar(input.read(), shift)
            
            with open(output, "w") as output:
                output.write(text)
# alphabet = string.ascii_uppercase

def caesar(text:str, key:int):
    text = text.upper()
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


if __name__ == "__main__":
    main()