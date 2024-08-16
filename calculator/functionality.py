import decimal
import numpy
from decimal import Decimal


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, decimal.InvalidOperation):
            return 'Enter the argument for the command.'
        except decimal.DivisionByZero:
            return 'Can\'t divide by zero.'

    return inner


@input_error
def parse_input(user_input: str):
    command, *args = user_input.strip().lower().split()
    args = [Decimal(num) for num in args]
    return command, *args


@input_error
def add_num(args):
    num1, num2, *_ = args
    return f'{num1} + {num2} = {num1 + num2}'


@input_error
def sub_num(args):
    num1, num2, *_ = args
    return f'{num1} - {num2} = {num1 - num2}'


@input_error
def mul_num(args):
    num1, num2, *_ = args
    return f'{num1} * {num2} = {num1 * num2}'


@input_error
def div_num(args):
    num1, num2, *_ = args
    return f'{num1} / {num2} = {num1 / num2}'


@input_error
def floor_div_num(args):
    num1, num2, *_ = args
    return f'{num1} // {num2} = {num1 // num2}'


@input_error
def pow_num(args):
    num1, num2, *_ = args
    return f'{num1} ** {num2} = {num1 ** num2}'


@input_error
def sqrt_num(args):
    num1, *_ = args
    return f'√{num1} = {numpy.sqrt(num1)}'
