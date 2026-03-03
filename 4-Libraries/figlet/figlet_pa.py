from pyfiglet import Figlet
from random import randint

figlet = Figlet()

fonts = figlet.getFonts()

f = input('Enter a font name or leave blank for random: ')
if f in fonts:
    figlet.setFont(font=f)
else:
    random_font_id = randint(0,(len(fonts)-1))
    f = fonts[random_font_id]
    figlet.setFont(font=f)

text = str(input('Enter text: '))
print(figlet.renderText(text))