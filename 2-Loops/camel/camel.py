def main():
    word = input('Enter a variable name: ')
    new_word = ''
    for letter in word:
        temp_letter = letter
        if letter.isupper():
            temp_letter = '_' + letter
            temp_letter = temp_letter.lower()
        new_word = new_word + temp_letter
    print(new_word)


if __name__ == "__main__":
    print(main())