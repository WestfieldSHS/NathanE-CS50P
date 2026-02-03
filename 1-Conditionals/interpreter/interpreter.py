def main():
    expression = input('Enter a mathematical expression: ')
    if " " in expression:
        x, y, z = expression.split(" ")
    else:
        print('Error: Invalid Expression, missing spaces')
        return
    
    x = float(x)
    z = float(z)
    a = 0.0
    if y == '+':
        a = x + z
        print(a)
    elif y == '-':
        a = x - z
        print(a)
    elif y == '*':
        a = x * z
        print(a)
    elif y == '/':
        if z == 0:
            print('Error: cannot divide by zero')
        else:
            a = x / z
            print(a)
    else:
        print('Error: Invalid Expression')


if __name__ == "__main__":
    print(main())