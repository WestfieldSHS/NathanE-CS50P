def main():
    time = input('Time? ')
    time = convert(time)
    print(time)
    if time > 7 and time < 8:
        print('breakfast time')
    elif time > 12 and time < 13:
        print('lunch time')
    elif time > 18 and time < 19:
        print('dinner time')
    


def convert(time):
    hours, minutes = time.split(':')
    minutes = float(minutes)
    minutes = minutes / 60
    hours = float(hours)
    time = hours + minutes
    return(time)

if __name__ == "__main__":
    print(main())