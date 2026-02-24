items = {}
def main():
    while True:
        try:
            item = input('Item: ')
        except EOFError:
            continue
        item = item.upper()
        if item not in items:
            items.update({item:1})
        else:
            quant = items[item]
            quant = quant + 1
            items.update({item:quant})
        print(items)
            
if __name__ == '__main__':
    main()