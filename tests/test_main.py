from app.main import calculate_discount


def test_calculate_discount():
    assert calculate_discount(100, 0.10) == 90
