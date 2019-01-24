"""Unit tests for the errors module."""

import json


def api_route_for(route):
    """Construct an URL to the endpoint for given route."""
    return '/api/v1/' + route


def get_json_from_response(response):
    """Decode JSON from response."""
    return json.loads(response.data.decode('utf8'))


def test_readiness_endpoint(client):
    """Test the /api/v1/readiness endpoint."""
    response = client.get(api_route_for("readiness"))
    assert response.status_code == 200
    json_data = get_json_from_response(response)
    assert json_data == {}, "Empty JSON response expected"


def test_readiness_endpoint_wrong_http_method(client):
    """Test the /api/v1/readiness endpoint by calling it with wrong HTTP method."""
    url = api_route_for("readiness")
    response = client.post(url)
    assert response.status_code == 405
    response = client.put(url)
    assert response.status_code == 405
    response = client.patch(url)
    assert response.status_code == 405
    response = client.delete(url)
    assert response.status_code == 405


def test_liveness_endpoint(client):
    """Test the /api/v1/liveness endpoint."""
    response = client.get(api_route_for("liveness"))
    assert response.status_code == 200
    json_data = get_json_from_response(response)
    assert json_data == {}, "Empty JSON response expected"


def test_liveness_endpoint_wrong_http_method(client):
    """Test the /api/v1/liveness endpoint by calling it with wrong HTTP method."""
    url = api_route_for("liveness")
    response = client.post(url)
    assert response.status_code == 405
    response = client.put(url)
    assert response.status_code == 405
    response = client.patch(url)
    assert response.status_code == 405
    response = client.delete(url)
    assert response.status_code == 405


def test_ingest_endpoint_wrong_http_method(client):
    """Test the /api/v1/ingest endpoint with wrong method."""
    response = client.get(api_route_for("ingest"))
    assert response.status_code == 405


def test_ingest_endpoint_wrong_content_type(client):
    """Test the /api/v1/ingest endpoint with wrong content-type."""
    headers = {
        'Content-Type': 'image/gif'
    }
    response = client.post(api_route_for("ingest"), headers=headers)
    assert response.status_code == 400
    json_data = get_json_from_response(response)
    assert "success" in json_data
    assert "summary" in json_data
    assert not json_data["success"]
    assert json_data["summary"] == "Set content type to application/json"


if __name__ == '__main__':
    test_readiness_endpoint()
    test_readiness_endpoint_wrong_http_method()
    test_liveness_endpoint()
    test_liveness_endpoint_wrong_http_method()
    test_ingest_endpoint_wrong_http_method()
    test_ingest_endpoint_wrong_content_type()
