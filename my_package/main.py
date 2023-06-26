import argparse
from module1.module1 import sum_numbers
from module2.module2 import multiply_numbers

def main():
    parser = argparse.ArgumentParser(prog='my_package')
    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')

    # Subcommand 'sum'
    sum_parser = subparsers.add_parser('sum')
    sum_parser.add_argument('numbers', nargs='+', type=int)
    sum_parser.set_defaults(func=sum_numbers)

    # Subcommand 'multiply'
    multiply_parser = subparsers.add_parser('multiply')
    multiply_parser.add_argument('numbers', nargs='+', type=int)
    multiply_parser.set_defaults(func=multiply_numbers)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        result = args.func(args.numbers)
        print(result)

if __name__ == '__main__':
    main()
