from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding, hashes

def generer_iv():
    # Générer un IV aléatoire
    iv = hashes.Hash(hashes.SHA256(), backend=default_backend())
    iv.update(b"initialisation_de_iv_aleatoire")
    iv = iv.finalize()[:16]
    return iv

def chiffrement_AES(cle, iv, message):
    # Créer un objet AES avec la clé spécifiée
    cipher = Cipher(algorithms.AES(cle), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Appliquer le padding au message
    padder = padding.PKCS7(128).padder()
    message_padded = padder.update(message) + padder.finalize()
    
    # Chiffrer le message
    message_chiffre = encryptor.update(message_padded) + encryptor.finalize()
    
    return message_chiffre


def dechiffrement_AES(cle, iv, donnees_chiffrees):
    # Créer un objet AES avec la clé et l'IV spécifiés
    cipher = Cipher(algorithms.AES(cle), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Déchiffrer les données
    donnees_dechiffrees = decryptor.update(donnees_chiffrees) + decryptor.finalize()
    
    return donnees_dechiffrees

# Exemple d'utilisation
cle = b'0123456789abcdef'  # Clé de 16 octets
iv = generer_iv() # Vecteur d'initialisation de 16 octets
message = b'Message a chiffrer'

message_chiffre = chiffrement_AES(cle, iv, message)
print("Message chiffré :", message_chiffre.hex())
message_dechiffre = dechiffrement_AES(cle,iv,message_chiffre)
print("Message dechiffre : ", message_dechiffre.decode())