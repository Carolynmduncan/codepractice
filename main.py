alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 

def encrypt(direction, text, shift):
  text = list(text)
  shift = int(shift)
  #Shifts each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text. 
  if direction.lower() == "encode":
    text = text[-shift:] + text[:-shift] 
  #To decode an encrypted mssage, shifts the 'text' back by the original shift amount and prints the decrypted text.
  if direction.lower() == "decode":
    text = text[+shift:] + text[:+shift]
  print(text)

encrypt(direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n"), text = input("Type your message:\n").lower(), shift = int(input("Type the shift number:\n")))

