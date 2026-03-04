from random import randint


def main():
    level = get_level()
    num1 = generate_integer(level)
    num2 = generate_integer(level)
    print(num1)
    print(num2)



def get_level():
    while True:
        try:
            level = int(input('Enter a level (1-3): '))
            if level < 1:
                raise ValueError
            if level > 3:
                raise ValueError
        except ValueError:
            continue
        break
    return level



def generate_integer(level):
    first_run = True
    num_str = ''
    for i in range(level):
        if first_run:
            digit = randint(1,9)
            first_run = False
        else:
            digit = randint(0,9)
        digit = str(digit)
        num_str = num_str + digit
    num_int = int(num_str)
    return(num_int)




if __name__ == "__main__":
    main()