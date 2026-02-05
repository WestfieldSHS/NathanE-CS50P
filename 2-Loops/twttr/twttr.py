def main():
    word = input('Enter a word: ')
    replacements = {"a": "", "e": "", "i": "", "o": "", "u": "", "A": "", "E": "", "I": "", "O": "", "U": ""}

    for old, new in replacements.items():
        word = word.replace(old,new)
    
    print(word)


if __name__ == "__main__":
    print(main())