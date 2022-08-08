## Test for 200 status code on user route


def test_response_200(api):
	response = api.get('/')
	assert response.status_code == 200



def test_post_user_valid(api,mocker):
	data = {"username":"something","first-name":"mildred","last-name":"jwt","email":"fake@email.cors"}
	mocker.patch("enviromates.routes.users.Users.query")
	response = api.post("/users/register", data=data)

# Test POST to /users with valid data to mock database using pytest-mock
# def test_post_user_valid(api,mocker):
# 	data = {"username":"tommy","password":"password"}
# 	mocker.patch("enviromates.routes.users.Users.query")
# 	response = api.post("/users/",data=data)
# 	assert response.status_code == 200
# 	assert "user created: username:tommy password:" in response.text

# Test GET user by id
def test_get_user_by_id(api):
	response = api.get("/users/1")
	assert response.status_code == 200
	print(response.text)
	assert '"username": "summ"' in response.text


# Test POST to /users
# this was just an experiment . can use it as reference but needs to be removed.
def test_post_user(api):
	data = {"username":"tommy","password":"password"}
	response = api.post("/users/",data=data)
	assert response.status_code == 200
	







