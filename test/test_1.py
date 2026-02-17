import requests

API_BASE_URL = "https://jsonplaceholder.typicode.com"


def test_should_get_post_by_id():
    get_response = requests.get(f"{API_BASE_URL}/posts/1")

    assert get_response.status_code == 200

    post_data = get_response.json()
    assert post_data["id"] == 1
    assert "title" in post_data
    assert "body" in post_data


def test_should_create_new_post():
    new_post_payload = {
        "title": "title",
        "body": "body",
        "userId": 1
    }

    create_response = requests.post(
        f"{API_BASE_URL}/posts",
        json=new_post_payload
    )

    assert create_response.status_code == 201

    created_post = create_response.json()
    assert created_post["title"] == new_post_payload["title"]
    assert created_post["body"] == new_post_payload["body"]
    assert "id" in created_post


def test_should_update_existing_post():
    update_post_payload = {
        "id": 1,
        "title": "title1",
        "body": "body1",
        "userId": 1
    }

    update_response = requests.put(
        f"{API_BASE_URL}/posts/1",
        json=update_post_payload
    )

    assert update_response.status_code == 200

    updated_post = update_response.json()
    assert updated_post["title"] == update_post_payload["title"]
