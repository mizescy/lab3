import lab2.Lab2 as lab2

def test_find_min_max():
    # Test with a typical list of numbers
    data = [10, 20, 30, 40, 50]
    min_val, max_val = lab2.find_min_max(data)
    assert min_val == 10, f"Expected min value 10, but got {min_val}"
    assert max_val == 50, f"Expected max value 50, but got {max_val}"

    # Test with all equal numbers
    data = [5, 5, 5, 5]
    min_val, max_val = lab2.find_min_max(data)
    assert min_val == 5, f"Expected min value 5, but got {min_val}"
    assert max_val == 5, f"Expected max value 5, but got {max_val}"

    # Test with negative numbers
    data = [-10, -20, -30, -40, -50]
    min_val, max_val = lab2.find_min_max(data)
    assert min_val == -50, f"Expected min value -50, but got {min_val}"
    assert max_val == -10, f"Expected max value -10, but got {max_val}"

def test_calc_average():
    # Test with a typical list of numbers
    data = [10, 20, 30, 40, 50]
    result = lab2.calc_average(data)
    assert result == 30, f"Expected average 30, but got {result}"

    # Test with all equal numbers
    data = [5, 5, 5, 5]
    result = lab2.calc_average(data)
    assert result == 5, f"Expected average 5, but got {result}"

    # Test with negative numbers
    data = [-10, -20, -30, -40, -50]
    result = lab2.calc_average(data)
    assert result == -30, f"Expected average -30, but got {result}"

def test_calc_median_temperature():
    # Test with an odd number of elements
    data = [30.0, 25.5, 28.0, 29.5, 27.0]
    result = lab2.calc_median_temperature(data)
    assert result == 28.0, f"Expected median 28.0, but got {result}"

    # Test with an even number of elements
    data = [10, 20, 30, 40]
    result = lab2.calc_median_temperature(data)
    assert result == 25.0, f"Expected median 25.0, but got {result}"

    # Test with all equal elements
    data = [5, 5, 5, 5, 5]
    result = lab2.calc_median_temperature(data)
    assert result == 5, f"Expected median 5, but got {result}"
