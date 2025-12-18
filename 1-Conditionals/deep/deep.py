def main():
    answer = input("What is the meaning of life, the universe and everything? ")
    answer = answer.lower()
    if answer == "42" or answer == "forty two" or answer == "forty-two":
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    print(main())
