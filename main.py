from functionality import parse_input, add_num, sub_num, mul_num, div_num, floor_div_num, pow_num, sqrt_num


def main():
    print('Welcome, this is calculator.')
    while True:
        command, *args = parse_input(input('Enter a command:'))
        if command == 'add':
            print(add_num(args))
        elif command == 'sub':
            print(sub_num(args))
        elif command == 'mul':
            print(mul_num(args))
        elif command == 'div':
            print(div_num(args))
        elif command == 'floor-div':
            print(floor_div_num(args))
        elif command == 'pow':
            print(pow_num(args))
        elif command == 'sqrt':
            print(sqrt_num(args))
        else:
            print('Unknown command.')


if __name__ == '__main__':
    main()
