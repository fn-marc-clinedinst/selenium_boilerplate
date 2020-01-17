from datetime import datetime
from random import choice


def add(number_one, number_two):
    return number_one + number_two


def subtract(number_one, number_two):
    return number_one - number_two


def multiply(number_one, number_two):
    return number_one * number_two


def static_greeting():
    return 'Hello, Stranger!'


def dynamic_greeting(name):
    return f'Hello, {name}!'


def dynamic_xpath(action_text):
    return f'//p[text()="{action_text}"]//ancestor::tr//i[@class="ion-trash-b"]'


def get_random_number():
    return choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def get_todays_date():
    date = datetime.now()

    return f'{date.month}/{date.day}/{date.year}'
