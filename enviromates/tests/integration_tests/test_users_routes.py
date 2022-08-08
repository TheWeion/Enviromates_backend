## Test for 200 status code on user route


def test_response_200(api):
	response = api.get('/')
	assert response.status_code == 200

# # Test POST to /users
# def test_post_user_valid(api,mocker):
# 	data = {"username":"tommy","password":"password"}
# 	mocker.patch("enviromates.routes.users.Users.query")
# 	response = api.post("/users/",data=data)
# 	assert response.status_code == 200
# 	assert "user created: username:tommy password:" in response.text

# def test_post_user_fail(api,mocker):
# 	data = {"name":"something"}
# 	mocker.patch("enviromates.routes.users.Users.query")
# 	response = api.post("/users/")	

def test_post_user_valid(api,mocker):
	data = {"username":"something","first-name":"mildred","last-name":"jwt","email":"fake@email.cors"}
	mocker.patch("enviromates.routes.users.Users.query")
	response = api.post("/users/register", data=data)
	assert response.status_code == 200
	
# def test_GET_user_valid(api,mocker):
# 	data = {"username":"something","first-name":"mildred","last-name":"jwt","email":"fake@email.cors"}
# 	mocker.patch("enviromates.routes.users.Users.query")
# 	new_user = api.post("/users/register", data=data)
# 	user = json.load(new_user)
# 	response = api.get(f"/users/{user['id']}")
# 	assert response.status_code == 200
# 	assert "username" in response.text



# 	response = api.get("/users/0")
# 	assert response.status_code == 200
# 	assert response.json == {"user":"user"}




# # Check if token has been generated for user
# def test_token_generated(api):
#     # Generate token for user
#     token = api.generateToken(1)
#     # Check if token is valid
#     assert api.verifyToken(token) == True
#     # Check if token is invalid
#     assert api.verifyToken("invalid token") == False
#     # Check if token is valid with wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id
#     assert api.verifyToken(token, user_id=1) == True
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verifyToken(token, user_id=2) == False
#     # Check if token is valid with correct user_id and wrong user_id
#     assert api.verify