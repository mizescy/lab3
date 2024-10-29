import lab2.Bmi as bmi

def test_bmi_under_weight():
    weight = 50  # kg
    height = 1.85  # meters
    result = bmi.calculate_bmi(height, weight)

def test_bmi_normal_weight():
    weight = 70  # kg
    height = 1.75  # meters
    result = bmi.calculate_bmi(height, weight)

def test_bmi_over_weight():
    weight = 85  # kg
    height = 1.65  # meters
    result = bmi.calculate_bmi(height, weight)