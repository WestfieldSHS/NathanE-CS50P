import sys
from pyfiglet import Figlet
from random import randint
from colorama import Fore

figlet = Figlet()
fonts = figlet.getFonts()
colors = ['RED','GREEN','BLUE','YELLOW','MAGENTA','CYAN','WHITE']

def set_color(c):
    match c:
        case 'RED':
            c = Fore.RED
            return c
        case 'GREEN':
            c = Fore.GREEN
            return c
        case 'BLUE':
            c = Fore.BLUE
            return c
        case 'YELLOW':
            c = Fore.YELLOW
            return c
        case 'MAGENTA':
            c = Fore.MAGENTA
            return c
        case 'CYAN':
            c = Fore.CYAN
            return c
        case 'WHITE':
            c = Fore.WHITE
            return c
        case _:
            c = Fore.WHITE
            return c


if len(sys.argv) == 1:
    random_font_id = randint(0,(len(fonts)-1))
    f = fonts[random_font_id]
    figlet.setFont(font=f)
    c = colors[randint(0,(len(colors)-1))]
    c = set_color(c)

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = sys.argv[2]
        if f in fonts:
            figlet.setFont(font=f)
            c = colors[randint(0,(len(colors)-1))]
            c = set_color(c)
        else:
            sys.exit("Invalid font name.")
    else:
        sys.exit("Invalid usage. First argument must be -f or --font.")
elif len(sys.argv) == 5:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = sys.argv[2]
        if f in fonts:
            figlet.setFont(font=f)
        else:
            sys.exit("Invalid font name.")
    else:
        sys.exit("Invalid usage. First argument must be -f or --font.")
    if sys.argv[3] == "-c" or sys.argv[3] == "--color":
        c = sys.argv[4].upper()
        if c in colors:
            c = set_color(c)
        else:
            sys.exit("Invalid color name.")
    else:
        sys.exit("Invalid usage. Second argument must be -c or --color.")
else:
    sys.exit("Usage: python figlet.py [-f FONT, -c COLOR]")

text = str(input('Enter text: '))
print(f'{c}{figlet.renderText(text)}')