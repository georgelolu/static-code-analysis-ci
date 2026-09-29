"""Tests for the application functions."""

from app.main import calculate_discount


def test_calculate_discount():
    """Verify that the discount calculation returns the expected price."""
    assert calculate_discount(100, 0.10) == 90
