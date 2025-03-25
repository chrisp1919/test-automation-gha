from main import factorials


def test_negative_factorial():
    result = list(factorials(-5))
    assert result == []


def test_zero_factorial():
    result = list(factorials(0))
    assert result == [1]


def test_positive_factorial():
    result = list(factorials(5))
    assert result == [1, 2, 6, 24, 120]


def test_fraction_factorial():
    try:
        result = list(factorials(0.75))
        assert result == []
    except TypeError as e:
        print("For fraction number is: {}".format(e))
