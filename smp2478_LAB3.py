"""
Name: Shivani Panchiwala
StudentID: 1001982478
Date: 2nd April 2023
OS: maxOs
Python Version: 3.11.2
"""

import os


def main():
    process_file('input_RPN.txt')


def process_file(filename):
    current_dir = os.getcwd()
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }

    full_path = os.path.join(current_dir, filename)

    with open(full_path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            ans = evaluate_rpn(line, operators)
            print(ans)
    file.close()


def evaluate_rpn(line, operators):
    line_data = line.split()
    stack = []

    for x in line_data:

        if x in operators:
            b, a = stack.pop(), stack.pop()
            result = operators[x](a, b)
            stack.append(result)
        elif '0' <= x <= '9':
            stack.append(int(x))
        else:
            print('Invalid operation provided for input =', x)
            return
    return stack[0]


if __name__ == '__main__':
    main()
