keyMatrix= [[0]*3 for i in range(3)]  
messagevector= [[0] for i in range(3)]  
cipherMatrix= [[0] for i in range(3)]  


def getKeyMatrix(key):
    k=0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j]=ord(key[k])%65
            k +=1

def encrypt(messagevector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j]=0
            for x in range(3):
                cipherMatrix[i][j]+= (keyMatrix[i][x]*messagevector[x][j])
            cipherMatrix[i][j]= cipherMatrix[i][j] %26    

def hillCipher(message, key):
    getKeyMatrix(key)

    for i in range(3):
        messagevector[i][0]= ord(message[i])%65

    encrypt(messagevector) 

    cipherText=[]
    for i in range(3):
        cipherText.append(chr(cipherMatrix[i][0]+65)) 


    print("".join(cipherText))   




message = 'ACT'
key= 'FTRKCWDML'

hillCipher(message,key)