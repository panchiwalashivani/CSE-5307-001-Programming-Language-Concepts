"""
Name: Shivani Panchiwala
StudentID: 100198248
Date: 2nd April 2023
OS: maxOS 
Python Version: 3.11.2
"""

""" The additional operator added here is the modulo division (%)"""

import os


def compute():

    curr_dir = os.getcwd()
    input_file = 'input_RPN_EC.txt'
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '%': lambda a, b: a % b
    }

    path = os.path.join(curr_dir, input_file)

    with open(path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            postfix = infix_to_postfix(line)
            print(postfix)
            ans = evaluate_postfix(postfix, operations)
            print(ans)
    f.close()


def infix_to_postfix(line):
    line_data = line.split()
    stack = []
    priority = {
        '-': 0,
        '+': 1,
        '*': 2,
        '/': 3,
        '%': 4
    }
    postfix = ''

    for x in line_data:
        if '0' <= x <= '9':
            postfix += x
        elif x == '(':
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and priority[x] <= priority[stack[-1]]:
                postfix += stack.pop()
            stack.append(x)
    while stack:
        postfix += stack.pop()
    return ' '.join(postfix)


def evaluate_postfix(line, operations):
    line_data = line.split()
    stack = []

    for x in line_data:

        if x in operations:
            b, a = stack.pop(), stack.pop()
            result = operations[x](a, b)
            stack.append(result)
        elif '0' <= x <= '9':
            stack.append(int(x))
        else:
            print('Invalid operation provided for input =', x)
            return
    return stack[0]


if __name__ == '__main__':
    compute()

