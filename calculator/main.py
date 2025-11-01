from functionality import (
    parse_input, add_num, sub_num, mul_num, div_num, floor_div_num, pow_num, sqrt_num,
    abs_num, mod_num, factorial_num, sin_num, cos_num, tan_num, log_num, ln_num,
    round_num, ceil_num, floor_num, show_help
)


def main():
    print('Welcome, this is calculator.')
    print('Type "help" to see available commands.\n')

    history = []

    while True:
        user_input = input('Enter a command: ')

        # Handle special commands that don't need parsing
        if user_input.strip().lower() in ('exit', 'close'):
            print('Bye!')
            break
        elif user_input.strip().lower() == 'help':
            print(show_help())
            continue
        elif user_input.strip().lower() == 'history':
            if history:
                print('\nCalculation history:')
                for i, calc in enumerate(history, 1):
                    print(f'{i}. {calc}')
            else:
                print('History is empty.')
            continue
        elif user_input.strip().lower() == 'clear-history':
            history.clear()
            print('History cleared.')
            continue

        # Parse and execute calculation commands
        command, *args = parse_input(user_input)
        result = None

        if command == 'add':
            result = add_num(args)
        elif command == 'sub':
            result = sub_num(args)
        elif command == 'mul':
            result = mul_num(args)
        elif command == 'div':
            result = div_num(args)
        elif command == 'floor-div':
            result = floor_div_num(args)
        elif command == 'pow':
            result = pow_num(args)
        elif command == 'mod':
            result = mod_num(args)
        elif command == 'sqrt':
            result = sqrt_num(args)
        elif command == 'abs':
            result = abs_num(args)
        elif command == 'factorial':
            result = factorial_num(args)
        elif command == 'sin':
            result = sin_num(args)
        elif command == 'cos':
            result = cos_num(args)
        elif command == 'tan':
            result = tan_num(args)
        elif command == 'log':
            result = log_num(args)
        elif command == 'ln':
            result = ln_num(args)
        elif command == 'round':
            result = round_num(args)
        elif command == 'ceil':
            result = ceil_num(args)
        elif command == 'floor':
            result = floor_num(args)
        else:
            result = 'Unknown command.'

        print(result)

        # Add successful calculations to history (not errors)
        if result and not any(error_msg in str(result) for error_msg in
                            ['Unknown command', 'Enter the argument', 'Can\'t divide',
                             'not defined', 'only defined']):
            history.append(result)


if __name__ == '__main__':
    main()
