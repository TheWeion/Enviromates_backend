import bcrypt
import jwt
from datetime import datetime, timedelta

def hashPassword(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")

def verifyPassword(password,hashedPassword):
    return bcrypt.checkpw(password.encode('utf-8'), hashedPassword.encode('utf-8'))

def generateToken(user_username):
    dt = datetime.now() + timedelta(days=7)
    return jwt.encode({'user_username': user_username,"exp":dt},'secret', algorithm='HS256')

def verifyToken(token):
    try:
        return  jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return 'signature has expired.'
    except:
        return 'Not Authorised.'