from student import calculate_total
from student import calculate_average

def test_total():
    assert calculate_total(85, 90, 80) == 255

def test_average():
    assert calculate_average(255) == 85
