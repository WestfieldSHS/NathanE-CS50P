fruits = {'apple':'130','avocado':'50','banana':'110','grapefruit':'60','grapes':'90','honeydew melon':'50','kiwifruit':'90','lemon':'15','lime':'20','nectarine':'60','orange':'80','peach':'60','pear':'100','pineapple':'50','plums':'70','strawberries':'50','sweet cherries':'100','tangerine':'50','watermelon':'80'}

def main():
    print('Fruit calorie checker.')
    choice = input('Enter a fruit: ')
    choice = choice.lower()
    if choice in fruits:
        print(f'Calories: {fruits[choice]}')
    return

if __name__ == "__main__":
    main()