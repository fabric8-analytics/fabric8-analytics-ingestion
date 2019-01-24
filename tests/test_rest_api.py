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


def test_liveness_endpoint(client):
    """Test the /api/v1/liveness endpoint."""
    response = client.get(api_route_for("liveness"))
    assert response.status_code == 200
    json_data = get_json_from_response(response)
    assert json_data == {}, "Empty JSON response expected"


def test_ingest_endpoint_wrong_method(client):
    """Test the /api/v1/ingest endpoint with wrong method."""
    response = client.get(api_route_for("ingest"))
    assert response.status_code == 405


if __name__ == '__main__':
    test_readiness_endpoint()
    test_liveness_endpoint()
    test_ingest_endpoint_wrong_method()
