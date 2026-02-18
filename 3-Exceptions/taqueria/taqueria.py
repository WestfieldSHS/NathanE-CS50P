menu = {
		"Baja Taco": 4.25,
		"Burrito": 7.50,
		"Bowl": 8.50,
		"Nachos": 11.00,
		"Quesadilla": 8.50,
		"Super Burrito": 8.50,
		"Super Quesadilla": 9.50,
		"Taco": 3.00,
		"Tortilla Salad": 8.00
	}

def main():
    while True:
        try:
            get_item()
        except EOFError:
            calculate_total()

        
def get_item():
    item = input('Enter a menu item: ')
    
def calculate_total():
    return


if __name__ == '__file__':
    main()