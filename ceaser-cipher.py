# Ceaser Cipher---

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




# Cease Cipher Logic
    
def ceaser(plain_text, cipher_shift, cipher_direction):
    cipher = ""
    if cipher_direction == "decode":
        cipher_shift *= -1
    for letter in plain_text:
        if letter in alphabets:
            position = alphabets.index(letter)    
            cipher += alphabets[position + cipher_shift]
        else:
            cipher += letter
    print(f"{cipher_direction}d message is: {cipher}")




is_restart = True
while is_restart:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ")
    text = input("Type your secret:\n").lower()
    shift = int(input("Shift to encrypt:\n"))
    shift = shift % 26
    ceaser(plain_text=text, cipher_shift=shift, cipher_direction=direction)
    restart = input("Type 'yes' to continue and 'no' to exit.\n")
    if restart == "no":
        is_restart = False
    else:
        isrestart = True
        



    