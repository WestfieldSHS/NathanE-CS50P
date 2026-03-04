from random import randint


def main():
    score = 0
    level = get_level()
    for i in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        answer = num1 + num2
        point = question(num1,num2,answer)
        score = score + point
    print(f'Score: {score}/10')



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

def question(num1, num2, answer):
    #num1,num2,answer = int(num1),int(num2),int(answer)
    attempt = 1
    while attempt < 4:
        try:
            guess = int(input(f'{num1} + {num2} = '))
        except ValueError:
            attempt = attempt + 1
            print('EEE')
            continue
        if guess == answer:
            print('Correct!')
            point = 1
            return point
        else:
            attempt = attempt + 1
            print('EEE')
            continue
    print(f'{num1} + {num2} = {answer}')
    point = 0
    return point


        


if __name__ == "__main__":
    main()