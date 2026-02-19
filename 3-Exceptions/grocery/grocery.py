
def main():
    while True:
        try:
            item = input('Item: ')
        except EOFError:
            continue
if __name__ == '__main__':
    main()