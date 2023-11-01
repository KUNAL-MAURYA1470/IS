s = input("Enter the string: ")
key = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c']

def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            r = (ord(char) - 97)
            result += key[r]
        else:
            result += char
    return result

encrypted_string = encrypt(s)
print("Encrypted string:", encrypted_string)


def decrypt(m):
    result = ""
    for char in m:
        if char.isalpha():
            for i in range(len(key)):
                if key[i] == char:
                    r = (i + 97)
                    result += chr(r)
                    break
        else:
            result += char
    return result

decrypted_string = decrypt(encrypted_string)
print("Decrypted string:", decrypted_string)
