import sys
from pyfiglet import Figlet
from random import randint

figlet = Figlet()
fonts = figlet.getFonts()


if len(sys.argv) == 1:
    random_font_id = randint(0,(len(fonts)-1))
    f = fonts[random_font_id]
    figlet.setFont(font=f)
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = sys.argv[2]
        if f in fonts:
            figlet.setFont(font=f)
        else:
            sys.exit("Invalid font name.")
    else:
        sys.exit("Invalid usage. First argument must be -f or --font.")
else:
    sys.exit("Usage: python figlet.py [-f FONT]")

text = str(input('Enter text: '))
print(f'{figlet.renderText(text)}')