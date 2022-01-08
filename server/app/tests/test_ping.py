"""tests the ping api routes app.api.ping.views.py"""

import json


def test_ping_200(test_app):
    client = test_app.test_client()
    resp = client.get("/api/v1/ping")
    data = json.loads(resp.data.decode())

    assert resp.status_code == 200
    assert "pong!" in data["message"]
