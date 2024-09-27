phrase = str(input(f"\ninput phrase you want ciphered\n\n>> "))
caesar_shift = int(input(f"\n\ninput the shift you want\n\n>> "))

def caesar_cipher(text: str, shift: int):
    result = ""

    for char in text:
        if char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.isdigit():
            result += chr((ord(char) + shift - 48) % 10 + 48)
        else:
            result += char
        
    return result

def caesar_decipher(secret: str, shift: int):
    result = ""

    for char in secret:
        if char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.isdigit():
            result += chr((ord(char) - shift - 48) % 10 + 48)
        else:
            result += char

    return result

message = caesar_cipher(phrase,caesar_shift)
print(f"\n\n{message}")

unciphered = caesar_decipher(message,caesar_shift)
print(f"\n\n\nunciphered message: {unciphered}")
