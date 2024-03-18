import bcrypt
from dotenv import load_dotenv
import os

def passwordCrypt(password: str):
    load_dotenv()
    passwordIncrypt = password.encode('utf-8')
    numberSalt = os.getenv('KEY_BCRYPT')
    salt = bcrypt.gensalt(int(numberSalt))
    hash_password = bcrypt.hashpw(password=passwordIncrypt,salt=salt)
    return hash_password

def checkPassword(password: str, checkPassword: bytes):
    load_dotenv()
    passwordIncrypt = password.encode('utf-8')
    if bcrypt.checkpw(password=passwordIncrypt,hashed_password=checkPassword):
        return True
    else:
        return False
    