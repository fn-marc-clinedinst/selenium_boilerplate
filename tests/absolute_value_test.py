"""
    Assignment: Write a function `absolute_value` that accepts a number as an argument and returns the number's
    absolute value. (Do not worry about non-numeric inputs.)

    Example run:
    >>> absolute_value(10)
    10
    >>> absolute_value(-10)
    10f
    >>> absolute_value(0)
    0

    To check that your implementation is correct, run the following command:

    pytest -m absolute_value -p no:warnings --log-cli-level info
"""
import logging
import pytest

from random import choice, uniform


def absolute_value(number):
    return number


@pytest.mark.absolute_value
class TestAbsoluteValue:
    @pytest.mark.parametrize('number', [-1, 0, 1])
    def test_integers_around_boundary(self, number):
        expected = abs(number)
        actual = absolute_value(number)

        logging.info(f'Verifying that absolute_value({number}) == {expected}')
        assert expected == actual

    @pytest.mark.parametrize('number', [-0.1, 0.0, 0.1])
    def test_floating_point_values_around_boundary(self, number):
        expected = abs(number)
        actual = absolute_value(number)

        logging.info(f'Verifying that absolute_value({number}) == {expected}')
        assert expected == actual

    @pytest.mark.parametrize('number', [choice(range(-1000000, 1000000)) for _ in range(10)])
    def test_some_random_integers(self, number):
        expected = abs(number)
        actual = absolute_value(number)

        logging.info(f'Verifying that absolute_value({number}) == {expected}')
        assert expected == actual

    @pytest.mark.parametrize('number', [uniform(-1000000, 1000000) for _ in range(10)])
    def test_some_random_floating_point_values(self, number):
        expected = abs(number)
        actual = absolute_value(number)

        logging.info(f'Verifying that absolute_value({number}) == {expected}')
        assert expected == actual
