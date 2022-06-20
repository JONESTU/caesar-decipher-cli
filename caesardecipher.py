import string
import os

print("Caesar Decipher by Tyshawn U. Jones")
print("Created approximately Sun 19 Jun 2022 11:21:05 PM EDT")
print("Completed approximately Sun 19 Jun 2022 11:31:43 PM EDT")
print("Description:")
print("Julius Caesar was an emperor who ciphered his messages by shifting the alphabet.")

user_printable = input("Enter the text to be deciphered: ")
user_shift = int(input("Enter the shift that the text was ciphered by: "))
reverse_shift = user_shift * (-1)

def caesar_decipher(user_printable, reverse_shift):
    ascii_characters = string.printable
    decipher_shift = ascii_characters[reverse_shift:] + ascii_characters[:reverse_shift]
    translation = user_printable.maketrans(ascii_characters, decipher_shift)
    return user_printable.translate(translation)

user_decipher = caesar_decipher(user_printable, reverse_shift)
print(user_decipher)
quit()

