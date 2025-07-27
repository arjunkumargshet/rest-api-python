
def test_create_user(user_api):
    payload = {"name": "Alice"}
    res = user_api.create_user(payload)
    assert res.status_code == 201
    assert res.json()["name"] == "Alice"
