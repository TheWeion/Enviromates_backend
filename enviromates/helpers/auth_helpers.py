import bcrypt
import jwt
from datetime import datetime, timedelta

def hashPassword(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verifyPassword(password,hashedPassword):
    return bcrypt.checkpw(password.encode('utf-8'), hashedPassword)

def generateToken(user_id):
    dt = datetime.now() + timedelta(days=7)
    return jwt.encode({'user_id': user_id,"exp":dt},'secret', algorithm='HS256')

def verifyToken(token):
    try:
        return jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return 'signature has expired.'
    except:
        return 'Not Authorised.'