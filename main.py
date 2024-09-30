import random

phrase = str(input(f"\nInput phrase you want ciphered\n\n>> "))
caesar_shift = int(input(f"\n\nInput the shift you want\n\n>> "))


charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def caesar_cipher(text: str, shift: int):
    result = ""
    for char in text:
        if char in charset:
            new_index = (charset.index(char) + shift) % len(charset)
            new_char = charset[new_index]
            if random.choice([True, False]):
                new_char = new_char.upper()
            else:
                new_char = new_char.lower()
            result += new_char
        else:
            result += char
    return result

def caesar_decipher(text: str, shift: int):
    result = ""
    for char in text:
        if char.lower() in charset:
            new_index = (charset.index(char.lower()) - shift) % len(charset)
            new_char = charset[new_index]
            if char.isupper():
                new_char = new_char.upper()
            else:
                new_char = new_char.lower()
            result += new_char
        else:
            result += char
    return result


secret_message = str(input(f"\nInput phrase you want ciphered\n\n>> "))
number = int(input(f"\n\nInput the shift you want\n\n>> "))

encrypted_message = caesar_cipher(secret_message, number)
print("Encrypted:", encrypted_message)
print("Decrypted:", secret_message)

#THIS CODE IS COPYRIGHTED BY KADEN HOOD