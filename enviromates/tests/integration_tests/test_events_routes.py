

## Test for 200 status code on user route
def test_get_events_response_200(api):
	response = api.get('/events/')
	print(response.json)
	assert response.status_code == 200

# def test_post_events_response_200(api):
# 	data = {
# 		"title":"Absolute mess on git-merge-close",
# 		"description":"i was walking my dog when two randoms decided to merge and it has destroyed the place. needs a good few hours to resolve.",
# 		"difficulty":"3",
# 		"start_date":"06/06/2022",
# 		"latitude":27830928703,
# 		"longitude":98270296,
# 		"img_before":"https://static.wixstatic.com/media/c6b13a_cc09af3ec41f45248ebd0cab36d9bef2~mv2.png/v1/fill/w_1110,h_738,al_c,q_90/c6b13a_cc09af3ec41f45248ebd0cab36d9bef2~mv2.webp",
# 		}
# 	response = api.post("/events/",data=data)
# 	print(response)
# 	assert response.status_code == 200
# 	assert "Event added." in response.text


# title = request.form["title"]
# 		description = request.form["description"]
# 		difficulty = request.form["difficulty"]
# 		start_date = request.form["start-date"]
# 		latitude = request.form["latitude"]
# 		longitude = request.form["longitude"]
# 		img_before = request.form["img-before"]
# 		new_event = Events(title=title, description=description, difficulty=difficulty, start_date=start_date, latitude=latitude, longitude=longitude, img_before=img_before)
# 		db.session.add(new_event)
# 		db.session.commit()
