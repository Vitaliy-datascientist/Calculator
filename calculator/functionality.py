import decimal
import numpy
import math
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


@input_error
def abs_num(args):
    num1, *_ = args
    return f'|{num1}| = {abs(num1)}'


@input_error
def mod_num(args):
    num1, num2, *_ = args
    return f'{num1} % {num2} = {num1 % num2}'


@input_error
def factorial_num(args):
    num1, *_ = args
    if num1 < 0:
        return 'Factorial is not defined for negative numbers.'
    if num1 != int(num1):
        return 'Factorial is only defined for integers.'
    return f'{int(num1)}! = {math.factorial(int(num1))}'


@input_error
def sin_num(args):
    num1, *_ = args
    return f'sin({num1}) = {Decimal(str(numpy.sin(float(num1))))}'


@input_error
def cos_num(args):
    num1, *_ = args
    return f'cos({num1}) = {Decimal(str(numpy.cos(float(num1))))}'


@input_error
def tan_num(args):
    num1, *_ = args
    return f'tan({num1}) = {Decimal(str(numpy.tan(float(num1))))}'


@input_error
def log_num(args):
    num1, *_ = args
    if num1 <= 0:
        return 'Logarithm is not defined for non-positive numbers.'
    return f'log10({num1}) = {Decimal(str(numpy.log10(float(num1))))}'


@input_error
def ln_num(args):
    num1, *_ = args
    if num1 <= 0:
        return 'Natural logarithm is not defined for non-positive numbers.'
    return f'ln({num1}) = {Decimal(str(numpy.log(float(num1))))}'


@input_error
def round_num(args):
    num1, *_ = args
    return f'round({num1}) = {round(num1)}'


@input_error
def ceil_num(args):
    num1, *_ = args
    return f'ceil({num1}) = {math.ceil(num1)}'


@input_error
def floor_num(args):
    num1, *_ = args
    return f'floor({num1}) = {math.floor(num1)}'


def show_help():
    help_text = """
Available commands:
  add <num1> <num2>       - Addition
  sub <num1> <num2>       - Subtraction
  mul <num1> <num2>       - Multiplication
  div <num1> <num2>       - Division
  floor-div <num1> <num2> - Floor division
  pow <num1> <num2>       - Power
  mod <num1> <num2>       - Modulo (remainder)
  sqrt <num>              - Square root
  abs <num>               - Absolute value
  factorial <num>         - Factorial (integers only)
  sin <num>               - Sine
  cos <num>               - Cosine
  tan <num>               - Tangent
  log <num>               - Logarithm base 10
  ln <num>                - Natural logarithm
  round <num>             - Round to nearest integer
  ceil <num>              - Round up
  floor <num>             - Round down
  history                 - Show calculation history
  clear-history           - Clear calculation history
  help                    - Show this help message
  exit, close             - Exit calculator
"""
    return help_text.strip()
