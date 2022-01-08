"""tests the movies api routes app.api.movies.views.py"""

import json


def test_movie_list_200(test_app, test_database):
    """MovieList.GET"""

    client = test_app.test_client()
    resp = client.get("/api/v1/movies")

    assert resp.status_code == 200
    assert resp.content_type == "application/json"


def test_movie_list_201(test_app, test_database):
    """MovieList.POST"""

    client = test_app.test_client()
    resp = client.post(
        "/api/v1/movies",
        content_type="application/json",
        data=json.dumps({
            "title": "test_movie_list_201",
            "description": "test_movie_list_201"
        })
    )

    assert resp.status_code == 201
    assert resp.content_type == "application/json"


def test_movie_get_200(test_app, test_database, add_movie):
    """MovieDetail.GET - 200"""

    _movie = add_movie("test_movie_get_200")
    client = test_app.test_client()
    resp = client.get(f"/api/v1/movies/{_movie.id}")

    assert resp.status_code == 200
    assert resp.content_type == "application/json"


def test_movie_get_404(test_app, test_database):
    """MovieDetail.GET - 404"""

    client = test_app.test_client()
    resp = client.get("/api/v1/movies/3242")
    data = json.loads(resp.data.decode())

    assert resp.status_code == 404
    assert "movie does not exist" in data["message"]


def test_movie_put_200(test_app, test_database, add_movie):
    """MovieDetail.PUT - 200"""

    _movie = add_movie("test_movie_put")
    client = test_app.test_client()
    resp = client.put(
        f"/api/v1/movies/{_movie.id}",
        content_type="application/json",
        data=json.dumps({
            "title": "test_movie_put_200",
            "description": "test_movie_put_200"
        })
    )

    assert resp.status_code == 200
    assert resp.content_type == "application/json"


def test_movie_put_404(test_app, test_database):
    """MovieDetail.PUT - 404"""

    client = test_app.test_client()
    resp = client.put(
        "/api/v1/movies/342343",
        content_type="application/json",
        data=json.dumps({
            "title": "does not exist",
            "description": "does not exist"
        })
    )
    data = json.loads(resp.data.decode())

    assert resp.status_code == 404
    assert "movie does not exist" in data["message"]


def test_movie_delete_204(test_app, test_database, add_movie):
    """MovieDetail.DELETE - 204"""

    _movie = add_movie("test_movie_delete")
    client = test_app.test_client()
    resp = client.delete(f"/api/v1/movies/{_movie.id}")

    assert resp.status_code == 204
    assert resp.content_type == "application/json"


def test_movie_delete_404(test_app, test_database):
    """MovieDetail.DELETE - 404"""

    client = test_app.test_client()
    resp = client.delete("/api/v1/movies/343243")
    data = json.loads(resp.data.decode())

    assert resp.status_code == 404
    assert "movie does not exist" in data["message"]
