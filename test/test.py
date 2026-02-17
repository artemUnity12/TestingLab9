import pytest
import requests

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


def test_get_post(base_url):
    response = requests.get(f"{base_url}/posts/1", timeout=5)

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")

    data = response.json()
    assert data["id"] == 1
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)


def test_create_post(base_url):
    payload = {
        "title": "title",
        "body": "body",
        "userId": 1
    }

    response = requests.post(
        f"{base_url}/posts",
        json=payload,
        timeout=5
    )

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert isinstance(data["id"], int)


def test_update_post(base_url):
    payload = {
        "id": 1,
        "title": "title1",
        "body": "body1",
        "userId": 1
    }

    response = requests.put(
        f"{base_url}/posts/1",
        json=payload,
        timeout=5
    )

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
