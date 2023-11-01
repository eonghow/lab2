import Lab2


def test_find_min_max():
    result = 5,10
    input_arr = [5,8,9,10]

    test_result = Lab2.calc_min_max(input_arr)

    assert (result == test_result)

def test_calc_average():
    result = 8
    input_arr = [5,8,9,10]

    test_result = Lab2.calc_average(input_arr)

    assert (result == test_result)

def test_calc_median_temperature():
    result = 8.5
    input_arr = [5,8,9,10]

    test_result = Lab2.medianlist(input_arr)

    assert (result == test_result)