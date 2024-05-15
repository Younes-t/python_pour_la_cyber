def encrypt(data:str,decal:int):
    encrypted_word=""
    for letter in data:
        letterd=chr(ord(letter)+decal)
        encrypted_word=encrypted_word+letterd
    return encrypted_word

def decrypt(data:str,decal:int):
    decal=-decal
    return encrypt(data,decal)

chiffrer=encrypt("younes est beau",5)
dechiffrer=decrypt(chiffrer,5)

print(chiffrer)
print(dechiffrer)