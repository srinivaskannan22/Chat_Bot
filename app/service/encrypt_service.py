from cryptography.fernet import Fernet

class Encrpt:

    def encrypt_(message: dict):
        with open ('secret.key','rb')as file :
            key=file.read()
        fernet=Fernet(key)    
        message['prompt']=fernet.encrypt(message['prompt'].encode())
        message['answer']=fernet.encrypt(message['answer'].encode())
        return message
    
    def decrypt_(message: dict):
        with open ('secret.key','rb')as file :
            key=file.read()
        fernet=Fernet(key)
        message['prompt']=fernet.decrypt(message['prompt']).decode()
        message['answer']=fernet.decrypt(message['answer']).decode()
        return message



