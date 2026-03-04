from random import randint

def main():
    while True:
        try:
            level = int(input('Level: '))
            if level < 1:
                raise ValueError
        except ValueError:
            print('ValueError: You must enter a positive integer')
            continue
        break

    target = randint(0,level)

    while True:
        try:
            guess = int(input('Guess? '))
            if guess < 1:
                raise ValueError
        except ValueError:
            print(f'ValueError: Guess must be a positive integer between 1 and {level}')
        
        if guess == target:
            print('Just right!')
            break
        elif guess > level:
            print(f'Too large, your guess should be between 1 and {level}.')
            continue
        elif guess < target:
            print('Too Small!')
            continue
        elif guess > target:
            print('Too large!')
            continue
        else:
            print("Don't know, guess again.")
            continue
    print('Thank you for playing!')


        

if __name__ == '__main__':
    main()