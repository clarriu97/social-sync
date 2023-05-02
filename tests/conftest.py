"""
This file is used to configure pytest.
"""
import pytest


@pytest.fixture.scope("session")
def test():
    """This is a test fixture."""
    return "test"
