months = {
		"January":1,
		"February":2,
		"March":3,
		"April":4,
		"May":5,
		"June":6,
		"July":7,
		"August":8,
		"September":9,
		"October":10,
		"November":11,
		"December":12
}

def date_validator(year, month, day):
    try:
        month,day = int(month),int(day)
    except ValueError:
        print('ValueError: Month or Day Value is not an integer.')
        return False
    
    if len(year) != 4:
        print('Invalid Year. Year must be entered as 4 digits.')
        return False
    elif year[0] != '1' and year[0] != '2':
        print('Invalid Year. This program only supports dates between 1000CE to 2999CE.')
        return False
    
    if month > 12:
        print('Invalid Month. Month cannot be a value greater than 12.')
        return False
    elif month < 1:
        print('Invalid Month. Month cannot be a value less than 1.')
    
    if month == 2:
        year = int(year)
        if year % 4:
            month_length = 29
        else:
            month_length = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        month_length = 30
    else:
        month_length = 31
    
    if day > month_length:
        print(f'Invalid Day. For month {month} a maximum of {month_length} is permitted.')
        return False
    elif day < 1:
        print('Invalid Day. Day cannot be less than 1.')
        return False
    
    return True

        


def main():
    while True:
        date_usa = input("Date: ")
        if '/' in date_usa:
            try:
                month,day,year = date_usa.split('/',3)
            except ValueError:
                print('Invalid date. Enter date as "MM/DD/YYYY" or "Month DD, YYYY"')
                continue
            if date_validator(year,month,day):
                month = month.zfill(2)
                day = day.zfill(2)
                break
            else:
                continue
        elif ',' in date_usa:
            try:
                month_word,day,year = date_usa.split(' ',3)
            except ValueError:
                print('Invalid date. Enter date as "MM/DD/YYYY" or "Month DD, YYYY"')
                continue
            month = str(months[month_word])
            day = day.replace(',','')
            if date_validator(year,month,day):
                month = month.zfill(2)
                day = day.zfill(2)
                break
            else:
                continue
        else:
            print('Invalid date. Enter date as "MM/DD/YYYY" or "Month DD, YYYY"')
            continue

    print(f'{year}-{month}-{day}')


if __name__ == '__main__':
    main()