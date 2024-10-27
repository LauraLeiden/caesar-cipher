# add your code here
alphabet = "abcdefghijklmnopqrstuvwxyz"

shift = 5
user_text = input("Please enter a sentence: ")
user_text = user_text.lower()

new_text = ""

for char in user_text:
    if char in alphabet:
        new_char = alphabet.find(char)
        new_char = (new_char + shift) % 26
        char = alphabet[new_char]
    new_text += char
    
print(new_text)