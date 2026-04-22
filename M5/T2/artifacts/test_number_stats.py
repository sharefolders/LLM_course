import number_stats

def test_mean_value():
    assert number_stats.mean_value([1, 2, 3]) == 2.0
    assert number_stats.mean_value([1, 2, 3, 4, 5]) == 3.0
    try:
        number_stats.mean_value([])
    except ValueError:
        pass  # Expected ValueError for empty list
    else:
        assert False, 'Expected ValueError not raised'

def test_median_value():
    assert number_stats.median_value([1, 2, 3]) == 2.0
    assert number_stats.median_value([1, 2, 3, 4]) == 2.5
    try:
        number_stats.median_value([])
    except ValueError:
        pass  # Expected ValueError for empty list
    else:
        assert False, 'Expected ValueError not raised'

def test_range_width():
    assert number_stats.range_width([1, 2, 3]) == 2
    assert number_stats.range_width([1, 5, 3]) == 4
    try:
        number_stats.range_width([])
    except ValueError:
        pass  # Expected ValueError for empty list
    else:
        assert False, 'Expected ValueError not raised'

def test_describe_numbers():
    result = number_stats.describe_numbers([1, 2, 3])
    assert result['count'] == 3
    assert result['mean'] == 2.0
    assert result['median'] == 2.0
    assert result['min'] == 1
    assert result['max'] == 3
    assert result['range_width'] == 2
    try:
        number_stats.describe_numbers([])
    except ValueError:
        pass  # Expected ValueError for empty list
    else:
        assert False, 'Expected ValueError not raised'


def run_tests():
    test_mean_value()
    test_median_value()
    test_range_width()
    test_describe_numbers()
    print('TESTS_PASSED')

if __name__ == '__main__':
    run_tests()