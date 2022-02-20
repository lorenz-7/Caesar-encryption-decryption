def caesar(text, key):
    sol = ''
    for i in range(len(text)):
      char = text[i]
      if (char.isupper()):
         sol += chr((ord(char) + key - 65) % 26 + 65)
      else:
         sol += chr((ord(char) + key - 97) % 26 + 97)
      return sol
text = (input("Letter:"))
key1 = int(input("Key: "))
print("Decrypted Letter: " + caesar(text, key1))





