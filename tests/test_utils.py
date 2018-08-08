"""Test module for classes and functions found in the utils module."""
from f8a_ingestion.utils import validate_request_data


def test_validate_request_data_not_valid_ecosystem():
    """Test the function validate_request_data."""
    payload = {}
    valid, message = validate_request_data(payload)
    assert not valid
    assert message == "Ecosystem name is not valid"


def test_validate_request_data_not_valid_backend():
    """Test the function validate_request_data."""
    payload = {"ecosystem": "foobar"}
    valid, message = validate_request_data(payload)
    assert not valid
    assert message == "Backend is not valid backend"

    payload = {"ecosystem": "foobar",
               "backend": "unknown"}
    valid, message = validate_request_data(payload)
    assert not valid
    assert message == "Backend is not valid backend"


def test_validate_request_data_valid_backend():
    """Test the function validate_request_data."""
    payload = {"ecosystem": "foobar",
               "backend": "npm"}
    valid, message = validate_request_data(payload)
    assert not valid
    assert message == "Backend is not valid backend"


if __name__ == '__main__':
    test_validate_request_data_not_valid_ecosystem()
    test_validate_request_data_not_valid_backend()
    test_validate_request_data_valid_backend()
