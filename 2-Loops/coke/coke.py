def main():
    amount_due = 50
    while amount_due > 0:
        print(f'Amount Due: {amount_due}')
        payment = int(input('Insert Coin: '))
        if payment == 25:
            amount_due = amount_due - payment
        elif payment == 10:
            amount_due = amount_due - payment
        elif payment == 5:
            amount_due = amount_due - payment
        else:
            print('Invalid coin inserted. Only 25, 10 and 5c coins accepted.')
    change = amount_due
    change = change * -1
    print(f'Change Owed: {change}')



if __name__ == "__main__":
    print(main())