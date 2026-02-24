items = {}
def main():
    while True: # infinte loop (until user ends with ctrl+d)
        try:
            item = input('Item: ') # ask for user input
        except EOFError: # unless user presses ctrl+d to end
            break # break from loop
        item = item.upper() # render user input in upper case, to avoid case sensitivity
        if item not in items: # if it is a new item, add to dictionary with quantity set to 1
            items.update({item:1})
        else: # else, increment the quantity
            quant = items[item]
            quant = quant + 1
            items.update({item:quant})
    # print a nice shopping list label
    print()
    print('-------------')
    print('SHOPPING LIST')
    print('-------------')
    
    # Sort the items dictionary alphabetically, output into new dictionary
    sorted_items = {}
    sorted_items = dict(sorted(items.items()))
    
    # This sorts the items by quantity in ascending order (I read the problem wrong!)
    # Still useful to have, so I left it here but commented out
    '''
    for key in sorted(items, key=items.get):
        sorted_items[key] = items[key]
    '''

    # iterate through the loop, printing out the quantity of each item and the item 
    for i in sorted_items:
        print(f'{sorted_items[i]} {i}')
            
if __name__ == '__main__':
    main()