"""Pytest suite for India State News API"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_all_news():
    res = client.get("/indnews")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
    assert len(res.json()) >= 5


def test_get_state_news():
    res = client.get("/indnews/maharashtra")
    assert res.status_code == 200
    assert res.json()["state"] == "Maharashtra"
    assert "Tech" in res.json()["title"]


def test_get_nonexistent_state():
    res = client.get("/indnews/nonexistent")
    assert res.status_code == 404
    assert "No news found" in res.json()["detail"]


def test_post_new_news():
    res = client.post("/indnews/teststate", json={
        "state": "Test",
        "title": "Test News",
        "short_description": "Test desc"
    })
    assert res.status_code == 201
    assert res.json()["state"] == "Teststate"


def test_post_validation_word_limit():
    long_text = " ".join(["word"] * 350)
    res = client.post("/indnews/test2", json={
        "state": "Test2",
        "title": "Title",
        "short_description": "Short",
        "full_description": long_text
    })
    assert res.status_code == 422
    assert "full_description" in str(res.json())


def test_delete_news():
    client.post("/indnews/delstate", json={
        "state": "Del",
        "title": "To Delete",
        "short_description": "Del desc"
    })
    res = client.delete("/indnews/delstate")
    assert res.status_code == 204
    res = client.get("/indnews/delstate")
    assert res.status_code == 404


def test_case_normalization():
    res = client.post("/indnews/UPPER", json={
        "state": "upper",
        "title": "Case Test",
        "short_description": "Test"
    })
    assert res.status_code == 201
    assert res.json()["state"] == "Upper"
