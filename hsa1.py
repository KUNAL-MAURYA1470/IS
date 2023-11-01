import hashlib

str_to_hash = input("Enter The string:")
result = hashlib.sha1(str_to_hash.encode())
print("The hexadecimal equivalent of SHA1 is: ", result.hexdigest())