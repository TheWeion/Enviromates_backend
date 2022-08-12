from enviromates.helpers.auth_helpers import hashPassword , verifyPassword,generateToken, verifyToken
import jwt
from time import sleep


# password hashes with a given string as request.form["password"]
def test_password_hashing():
    # predefine password to get length
    password = "test_password"
    # attempt hashPassword
    result = hashPassword(password)
    # check that the length of str(password) is massive through hash/salt
    assert len(result) > len(password)


# verify password returns true if correct password given
def test_password_verification_success():
    # predefine what a hashed password would look like
    hashedPassword = hashPassword("test_password")
    # verify login attempt password with stored password
    result = verifyPassword("test_password",hashedPassword)
    assert result == True

# verify password FAILS if incorrect password given
def test_password_verification_fail():
    #predefine what hashed password would look like
    hashedPassword = hashPassword("test_password")
    # verify password from user vs stored password
    result = verifyPassword("wrong_password", hashedPassword)
    assert result == False

# generates a valid jsonwebtoken containing user_id within the payload
def test_accesstoken_generation_success():
    # a mock user id as primary_key
    user_id = "uaypw948tawhi"
    token = generateToken(user_id)
    assert "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9" in token

def test_accesstoken_verification_success():
    # create a brand new token
    token = generateToken("test_user_username")
    # try to verify the token
    result = verifyToken(token)
    # confirms a token is NOT invalid
    assert result != False
    # returns the user_id from within the payload
    assert "test_user_username" in result["user_username"]
    # returns expiry time from within the payload
    assert result["exp"] != None


def test_accesstoken_fail_on_expired():
    # create a token to expire in 1 second
    token = jwt.encode({'user_id': "user_id","exp":1},'secret', algorithm='HS256')
    # wait 1 second to ensure this token is expired
    sleep(1)
    # try to verify token through auth_helpers
    result = verifyToken(token)
    # should return expired
    assert result == "signature has expired."

def test_accesstoken_fail_on_tampered_secret():
    #create a genuine token with incorrect secret
    token = jwt.encode({'user_id': "user_id"},'incorrectsecret', algorithm='HS256')
    # attempt to validate foreign-secret token
    result = verifyToken(token)
    # test auth has invalidated token with incorrect secret
    assert result == 'Not Authorised.'
