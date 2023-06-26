import argparse
from my_package.sum.sum import sum_numbers
from my_package.multiply.multiply import multiply_numbers

def main():
    parser = argparse.ArgumentParser(prog='my_package')                               # 创建一个ArgumentParser对象，命名为parser，并指定了一个程序名称'my_package'
    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')        # 创建一个子命令解析器（subparsers），并设置一个标题'subcommands'和一个目标属性'subcommand'。

    # Subcommand 'sum'
    sum_parser = subparsers.add_parser('sum')                                         # 定义一个名为'sum'的子命令解析器sum_parser
    sum_parser.add_argument('numbers', nargs='+', type=int)                           # 调用sum_parser.add_argument方法，为'sum'子命令添加一个参数规则。使用'numbers'作为参数名，并指定nargs='+'表示可以接受一个或多个参数值，类型为整数（type=int）。
    sum_parser.set_defaults(func=sum_numbers)                                         # 调用sum_parser.set_defaults方法，将func属性设置为sum_numbers函数。当使用'sum'子命令时，程序会调用sum_numbers函数来处理该子命令。

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

