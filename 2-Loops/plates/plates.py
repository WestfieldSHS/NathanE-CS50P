letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

# Rule 1: “All vanity plates must start with at least two letters.”
def letter_start(plate):
    first_char = plate[0]
    second_char = plate[1]
    if first_char.lower() in letters:
        if second_char.lower() in letters:
            return True
        else:
            return False
    else: 
        return False 

# Rule 2: “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def plate_length(plate):
    plate_count = len(plate)
    if plate_count < 2:
        return False
    elif plate_count > 6:
        return False
    else:
        return True
    
# Rule 3: “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
def numbers_end(plate):
    number_started = False

    for char in plate:
        if char in digits:
            if not number_started:
                if char == '0':
                    return False
            number_started = True
        elif number_started and char in letters:
            return False
    return True

# Rule 4: “No periods, spaces, or punctuation marks are allowed.”
def no_punctuation(plate):
    for char in plate:
        char = char.lower()
        if char not in letters and char not in digits:
            return False
    return True

# Function to determine overall validity, if plate meets all rule requirements
def is_valid(plate):
    if plate_length(plate):
        if letter_start(plate):
            if numbers_end(plate):
                if no_punctuation(plate):
                    return True
                else:
                    # print('No Punctuation rule invalid.')
                    return False
            else:
                # print('Numbers end rule invalid.')
                return False
        else:
            # print('Letters start rule invalid.')
            return False
    else:
        # print('Plate length invalid.')
        return False


# Main function
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    
#Run program by calling main function
if __name__ == "__main__":
    main()