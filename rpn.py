#!/usr/bin/env python3

from colored import fore, back, style

def calculate(arg):
    stack = []

    tokens = arg.split()

    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            val2 = stack.pop()
            val1 = stack.pop()
            print(val1, end='')
            if token == '+':
                result = val1 + val2
                print(fore.GREEN + '+' + style.RESET, end='')
            elif token == '-':
                result = val1 - val2
                print (fore.RED + '-' + style.RESET, end='')
            elif token == '^':
                result = val1 ** val2
            elif token == '*':
                result = val1 * val2
                print (fore.YELLOW + '^' + style.RESET, end='')
            
            print(val2, end='')
            print(' ' + back.WHITE + fore.BLACK + '=' + style.RESET + ' ', end='')
            stack.append(result)

    if len(stack) > 1:
        raise ValueError('Too many arguments on the stack')

    return stack[0]

def main():
    while True:
        try:
            result = calculate(input('rpn <calc> '))
            print(result)
        except ValueError:
            pass

if __name__ == '__main__':
    main()

