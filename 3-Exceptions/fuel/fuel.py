def main():
    try: 
        fraction = input('Enter a fraction: ')
        x,y = fraction.split('/')
        x = int(x)
    except ValueError:
        print('x is not an integer')
    
    


if __name__ == "__main__":
    main()