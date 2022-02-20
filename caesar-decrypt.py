key = int(input("Brute-Force attempt with key (1-25): "))
# INSERT TEXT YOU WANT TO DECRYPT IN UPPERCASE INTO THE BRACKETS
encrypted_text = ("####INSERT TEXT####")
decrypted_text = ""
for i in encrypted_text:
    if i.isupper():
        ic = ord(i)
        ii = ord(i) - ord("A")
        ni = (ii - key) % 26
        nc = ni + ord("A")
        n_chr = chr(nc)
        decrypted_text = decrypted_text + n_chr   
    else:
        decrypted_text += i
        print("Sucessfull attempt to decrypt: ")
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)



