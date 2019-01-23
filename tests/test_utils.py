"""Test module for classes and functions found in the utils module."""
from f8a_ingestion.utils import validate_request_data, _eco_object_dict


def test_validate_request_data_no_payload():
    """Test the function validate_request_data: how it handles empty payload."""
    payload = None
    valid, message = validate_request_data(payload)
    assert not valid
    assert message == "Invalid: input is empty"


def test_validate_request_data_empty_payload():
    """Test the function validate_request_data: how it handles improper payload."""
    payload = {}
    valid, message = validate_request_data(payload)
    assert not valid
    assert message == "Invalid: input is empty"


def test_validate_request_data_not_valid_ecosystem():
    """Test the function validate_request_data: how it handles improper payload."""
    payload = {"foo": "bar"}
    valid, message = validate_request_data(payload)
    assert not valid
    assert message == "Ecosystem name is not valid"


def test_validate_request_data_not_valid_backend():
    """Test the function validate_request_data: how it handles improper payload."""
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
    """Test the function validate_request_data: how it handles proper payload."""
    payload = {"ecosystem": "foobar",
               "backend": "npm"}
    valid, message = validate_request_data(payload)
    assert valid
    assert message is None


def test_eco_object_dict():
    """Test the function _eco_object_dict."""
    data = {"ecosystem": "e",
            "url": "u",
            "backend": "b"}
    result = _eco_object_dict(data)
    assert result
    assert "ecosystem" in result
    assert "url" in result
    assert "backend" in result


if __name__ == '__main__':
    test_validate_request_data_no_payload()
    test_validate_request_data_empty_payload()
    test_validate_request_data_not_valid_ecosystem()
    test_validate_request_data_not_valid_backend()
    test_validate_request_data_valid_backend()
    test_eco_object_dict()
