"""Definition of fixtures for static data, sessions etc. used by unit tests."""

import pytest

from f8a_ingestion.rest_api import app


@pytest.fixture
def client():
    """Provide the client session used by tests."""
    with app.app.test_client() as client:
        yield client
