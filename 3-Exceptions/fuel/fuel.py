def main():
    fraction = get_fraction()
    x, y = split_fraction(fraction)
    z = fraction_to_percentage(x,y)
    print(f'Fuel Level: {display(z)}')

    
def get_fraction():
    fraction = input('Enter a fraction: ')
    return fraction

def split_fraction(fraction):
    try:
        x,y = fraction.split('/')
        x, y = int(x), int(y)
    except ValueError:
        print('ValueError: A value is not an integer')
        main()
    else:
        return x, y
    
def fraction_to_percentage(x,y):
    try:
        z = x / y * 100
    except ZeroDivisionError:
        print('ZeroDivisionError: Cannot divide by zero')
        main()
    else:
        if x > y:
            print('ValueError: Numerator is larger than denominator')
            main()
        z = int(z)
        return(z)

def display(z):
    if z <= 1:
        return('E')
    elif z >= 99:
        return('F')
    else:
        return(f'{z}%')
    
if __name__ == "__main__":
    main()