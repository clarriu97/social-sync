"""
This file is used to configure pytest.
"""
import pytest


@pytest.fixture(scope="session")
def test_hello_world():
    """This is a test fixture."""
    return "Hello World!"
