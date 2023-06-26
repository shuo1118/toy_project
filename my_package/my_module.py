import subprocess

def sum_numbers(numbers):
    result = subprocess.check_output(["python", "sum.py"] + [str(num) for num in numbers])
    return int(result)

def multiply_numbers(numbers):
    result = subprocess.check_output(["python", "multiply.py"] + [str(num) for num in numbers])
    return int(result)

