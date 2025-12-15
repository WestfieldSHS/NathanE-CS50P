def convert(message):
    if ":)" in message and ":(" in message:
        message = message.replace(":)", "🙂")
        message = message.replace(":(", "🙁")
        return message
    elif ":)" in message:
        return message.replace(":)", "🙂")
    elif ":(" in message:
        return message.replace(":(", "🙁")
    else:
        return message


def main():
    text = input("Enter text: ")
    print(convert(text))


if __name__ == "__main__":
    main()
