import random 
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "!@#-_"

def main():
    length = get_length()
    characters = get_characters()
    print(repr(characters))
    password = generate_password(length , characters)
    print(f"\nyour password is {password}")


def get_length():
    while True:
        try:
            length = int(input("enter password length:"))
            if length <= 0:
                print("Please enter a positive number.")
            else:
                return length
        except ValueError:
            print("PLEASE ENTER A  VALID NUMBER")
def get_characters():
    while True:
        characters = ""
        upper = input(" you want uppercase? y/n:").lower()
        lower = input(" you want lowercase? y/n:").lower()
        number = input(" you want numbers? y/n:").lower()
        symbol = input(" you want Symbols? y/n:").lower()
        if upper == "y":
            characters += UPPERCASE
        if lower == "y":
            characters += LOWERCASE
        if number == "y":
            characters += NUMBERS
        if symbol == "y":
            characters += SYMBOLS
        if characters == "":
            print("Please select at least one character type.\n")
        else:
            return(characters)
        
       

def generate_password(length , characters):
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return(password)


main()