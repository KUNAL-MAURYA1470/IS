def generatedKey(string ,key):
    key=list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i%len(key)])
        return ("".join(key))
    
def cipherText(string,key):
    cipher_text=[]
    for i in range(len(string)):
        x=(ord(string[i])+ord(key[i]))%26
        x+=ord('A')
        cipher_text.append(chr(x))
    return("".join(cipher_text))

def originalText(cipher_text,key):
    org_text=[]
    for i in range(len(cipher_text)):
        x=(ord(cipher_text[i])-ord(key[i])+26)%26
        x+=ord('A')
        org_text.append(chr(x))
    return("".join(org_text))
    

string= "HELLOWORLD"
keyword= "KUNAL"
key = generatedKey(string, keyword)
cipher_text = cipherText(string,key)
print("Ciphertext :", cipher_text)
print("Original/Decrypted Text :", originalText(cipher_text, key))
