import pytest

import main

@pytest.fixture(name="seven")
def fixture_seven():
    return 7

@pytest.mark.skip("Fix this someday")
def test_fail():
    """Check that everything works"""
    assert False


def test_pass(seven):
    """Check something cool"""
    assert seven == 8
