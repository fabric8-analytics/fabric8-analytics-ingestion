"""Unit tests for the errors module."""

import pytest
from f8a_ingestion.errors import F8AConfigurationException


def test_f8a_configuration_exception():
    """A sort of dummy test the basic behaviour of F8AConfigurationException class."""
    e = F8AConfigurationException("some message")
    assert e.__str__() == "some message"

    with pytest.raises(F8AConfigurationException) as e:
        raise F8AConfigurationException("some message")
    assert e


if __name__ == '__main__':
    test_f8a_configuration_exception()
