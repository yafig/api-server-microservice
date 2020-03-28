import hashlib
import string
import random
import binascii

def hash_password(password, salt):
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    print(binascii.hexlify(hashed_password))
    return binascii.hexlify(hashed_password)

def randomString(stringLength=32):
    """Generate a random string of fixed length """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=stringLength))