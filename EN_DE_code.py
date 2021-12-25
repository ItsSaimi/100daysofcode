alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(p_text, shift_a):
    cipher_text=""
    for letter in p_text:
        p = alphabet.index(letter)
        n_p = p + shift_a
        new_letter = alphabet[n_p]
        cipher_text += new_letter
    print(f"Encrypted text is '{cipher_text}'.")

#encrypt(p_text=text, shift_a=shift)

def decrypt(cipher_text, shift_a):
    p_text = ""
    for letter in cipher_text:
        p = alphabet.index(letter)
        n_p = p - shift_a
        new_letter = alphabet[n_p]
        p_text += new_letter
    print(f"Decrypted text is '{p_text}'.")

if direction == "encode":
  encrypt(p_text=text, shift_a=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_adecode=shift)
