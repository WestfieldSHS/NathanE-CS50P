import emoji


def main():
    text = input('Enter emoji text: ')
    text_output = emoji.emojize(text, language='alias')
    print(f'Output: {text_output}')

if __name__ == "__main__":
    main()