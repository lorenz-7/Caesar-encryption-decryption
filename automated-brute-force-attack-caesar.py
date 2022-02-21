x = 1
while x <= 25 and x > 0:
    #INSERT UPPERCASE TEXT INTO THE BRACKETS BELOW
    encrypt = ("####INSERT#####")
    decrypt = (" ")
    for i in encrypt:
        if i.isupper():
            ic = ord(i)
            ii = ord(i) - ord("A")
            ni = (ii - x) % 26
            nc = ni + ord("A")
            n_chr = chr(nc)
            decrypt = decrypt + n_chr   
        else:
            decrypt += i
    print("Decrypted text:" , x,decrypt)    
    x += 1