import argparse
import json
from my_package.sum.sum import sum_numbers
from my_package.multiply.multiply import multiply_numbers

def sum_numbers_func(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    numbers = data['number']['sum_number']
    result = sum_numbers(numbers)
    return result

def multiply_numbers_func(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    numbers = data['number']['multiply_number']
    result = multiply_numbers(numbers)
    return result

def main():
    parser = argparse.ArgumentParser(prog='my_package')                               # 创建一个ArgumentParser对象，命名为parser，并指定了一个程序名称'my_package'
    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')        # 创建一个子命令解析器（subparsers），并设置一个标题'subcommands'和一个目标属性'subcommand'。

    # Subcommand 'sum'
    sum_parser = subparsers.add_parser('sum')                                         # 定义一个名为'sum'的子命令解析器sum_parser
    sum_parser.add_argument('json_file', type=str, help='Path to the JSON file')      # 调用sum_parser.add_argument方法，为'sum'子命令添加一个参数规则。
    sum_parser.set_defaults(func=sum_numbers_func)                                    # 调用sum_parser.set_defaults方法，将func属性设置为sum_numbers函数。

    # Subcommand 'multiply'
    multiply_parser = subparsers.add_parser('multiply')
    multiply_parser.add_argument('json_file', type=str, help='Path to the JSON file')
    multiply_parser.set_defaults(func=multiply_numbers_func)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        result = args.func(args.json_file)
        print(result)

if __name__ == '__main__':
    main()
