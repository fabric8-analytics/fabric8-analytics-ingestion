"""Unit tests for the errors module."""

import pytest
from f8a_ingestion.rest_api import readiness


def test_readiness_endpoint():
    """Test the /api/v1/readiness endpoint."""
    response = client.get(api_route_for("readiness"))
    assert response.status_code == 200
    json_data = get_json_from_response(response)
    assert json_data == {}, "Empty JSON response expected"


if __name__ == '__main__':
    test_readiness()
