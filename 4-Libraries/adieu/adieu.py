import inflect #import inflect module

p = inflect.engine() #assign inflect engine to variable p for easier access to functions

def main():
    names = [] #a list of names, initially empty
    while True: #infinte loop until it is broken out of
        try:
            name = input('Name: ').strip() # ask user to input a name
        except EOFError: # break loop if ctrl+d is pressed
            break #break from loop
        names.append(name) # append name to names list
    joined_names = p.join(names) # use inflect.engine.join method to join using commas and 'and'
    print() # print blank line for clarity
    print(f'Adieu, adieu, to {joined_names}') # print output string as specified including inflect joined string

if __name__ == "__main__":
    main()