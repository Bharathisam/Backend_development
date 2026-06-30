from tests.conftest import client


def test_create_hero():
    response = client.post(
        "/heroes/",
        json={
            "name": "Batman",
            "age": 35,
            "secret_name": "Bruce Wayne"
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Batman"
    assert data["age"] == 35
    assert "id" in data


def test_create_hero_validation_error():
    response = client.post(
        "/heroes/",
        json={
            "name": "",
            "age": -5,
            "secret_name": ""
        },
    )

    assert response.status_code == 422

    data = response.json()

    assert data["error"]["code"] == 422
    assert data["error"]["message"] == "Validation Error"