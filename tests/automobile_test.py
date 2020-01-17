"""
    Assignment: Create a Python class named Automobile with the following attributes:

    * make -> The make of the automobile. (i.e., 'Honda')
    * model -> The model of the automobile. (i.e., 'Civic')
    * year -> The year the automobile was manufactured. (i.e., 2019)
    * current_speed -> The current speed of the vehicle. Should be initialized to 0.
    * accelerate -> Accepts an integer and increments the speed by that value.
    * decelerate -> Accepts an integer and decrements the speed by that value. (Going less than 0 is ok--consider it reverse.)

    To check that your implementation is correct, run the following command:

    pytest -m automobile -p no:warnings -v
"""
import pytest


class Automobile:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.current_speed = 0

    def accelerate(self, delta):
        self.current_speed += delta

    def decelerate(self, delta):
        self.current_speed -= delta


@pytest.mark.automobile
class TestAutomobile:
    @pytest.fixture
    def automobile(self):
        return Automobile('Honda', 'Civic', 2019)

    def test_automobile_has_correct_make(self, automobile):
        assert automobile.make == 'Honda'

    def test_automobile_has_correct_model(self, automobile):
        assert automobile.model == 'Civic'

    def test_automobile_has_correct_year(self, automobile):
        assert automobile.year == 2019

    def test_automobile_current_speed_is_initialized_to_0(self, automobile):
        assert automobile.current_speed == 0

    def test_automobile_can_accelerate(self, automobile):
        automobile.accelerate(10)

        assert automobile.current_speed == 10

    def test_automobile_can_decelerate(self, automobile):
        automobile.decelerate(5)

        assert automobile.current_speed == -5
