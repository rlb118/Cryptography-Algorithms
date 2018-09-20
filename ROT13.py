def letToNum(letter):
    #Convert letter to its related number (A = 1, B = 2, etc)
    if letter in letters:
        return ord(letter.upper()) - 64)
    return 0

def NumberToLetter(number):
    #convert number to its related letter
    letter = chr(((number - 1) % 26) + 65)
    return letter
    

text = input("Enter the text to encrypt/decrypt")
new_text = ""
for letter in text:
    new_text = new_text + NumberToLetter(letToNum(letter) + 13)
print(new_newText)
    