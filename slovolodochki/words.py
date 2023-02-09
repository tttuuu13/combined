from PIL import Image
import math


a = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я', 'ы']
b = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'й']
s_drop = Image.open('капля.png')
s_drop = s_drop.resize((62, 97))
b_drop = Image.open('капля.png')
b_drop = b_drop.resize((126, 195))
boat = Image.open('лодка.png')
boat = boat.resize((468, 128))



def word(word, is_text):
    width_total = (len(word) - 1) * 40 + 80
    widths = []
    chars = []
    new_line = False
    for char in word:
        try:
            if char == '?':
                img = Image.open('Буквы/q.png')
            elif char == ':':
                img = Image.open('Буквы/colon.png')
            elif char == '"':
                img = Image.open('Буквы/comas.png')
            elif char == '-' or char == '–' or char == '—':
                img = Image.open('Буквы/--scale-4_00x.png')
            else:
                img = Image.open('Буквы/' + char.upper() + '-scale-4_00x.png')
            width, height = img.size
        except:
            pass

        if char == char.upper():
            if char == 'Ё':
                img = img.resize((300 * width // height, 300), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Щ' or char == 'Ц':
                img = img.resize((240 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Й':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == '.':
                img = img.resize((60 * width // height, 60), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == ',':
                img = img.resize((100 * width // height, 100), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '"':
                img = img.resize((100 * width // height, 100), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '!':
                img = img.resize((290 * width // height, 290), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '?':
                img = img.resize((290 * width // height, 290), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '-':
                img = img.resize((150 * width // height, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '–':
                img = img.resize((150 * width // height + 150, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '—':
                img = img.resize((150 * width // height + 200, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == ':':
                img = img.resize((220 * width // height, 220), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == ';':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '*':
                new_line = True
            elif char == '_':
                width_total += 200
                widths.append(200)
                chars.append(Image.new('RGB', (200, 250), 'white'))
            else:
                img = img.resize((240 * width // height, 240), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
        else:
            if char == 'ё':
                img = img.resize((260 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'щ' or char == 'ц':
                img = img.resize((200 * width // height, 220), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'й':
                img = img.resize((230 * width // height, 230), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            else:
                img = img.resize((200 * width // height, 200), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue

    if is_text:
        bg = Image.new('RGB', (width_total, 540), 'white')
        x = 40
        index = 0
        for img in chars:
            if word[index] == 'Ё':
                bg.paste(img, (x, 0))
            elif word[index] == 'ё':
                bg.paste(img, (x, 40))
            elif word[index] == 'Й':
                bg.paste(img, (x, 20))
            elif word[index] == 'й':
                bg.paste(img, (x, 70))
            elif word[index] == '.':
                bg.paste(img, (x, 250))
            elif word[index] == ',':
                bg.paste(img, (x, 270))
            elif word[index] == ',':
                bg.paste(img, (x, 10))
            elif word[index] == '!':
                bg.paste(img, (x, 10))
            elif word[index] == '?':
                bg.paste(img, (x, 10))
            elif word[index] == ':':
                bg.paste(img, (x, 100))
            elif word[index] == ';':
                bg.paste(img, (x, 100))
            elif word[index] == '-' or word[index] == '–' or word[index] == '—':
                bg.paste(img, (x, 150))
            elif word[index] == word[index].upper():
                bg.paste(img, (x, 60))
            elif word[index] == word[index].lower():
                bg.paste(img, (x, 100))
            x += widths[index] + 40
            index += 1
        drop_y = 340
        boat_y = 260
    else:
        bg = Image.new('RGB', (width_total, 500), 'white')
        x = 40
        index = 0
        for img in chars:
            if word[index] == 'ё':
                bg.paste(img, (x, 0))
            elif word[index] == 'й':
                bg.paste(img, (x, 30))
            elif word[index].upper() == '.':
                bg.paste(img, (x, 230))
            elif word[index] == ',':
                bg.paste(img, (x, 230))
            elif word[index] == '"':
                bg.paste(img, (x, 10))
            elif word[index] == '!':
                bg.paste(img, (x, 0))
            elif word[index] == '?':
                bg.paste(img, (x, 0))
            elif word[index] == ':':
                bg.paste(img, (x, 60))
            elif word[index] == ';':
                bg.paste(img, (x, 60))
            elif word[index] == '-' or word[index] == '–' or word[index] == '—':
                bg.paste(img, (x, 110))
            else:
                bg.paste(img, (x, 60))
            x += widths[index] + 40
            index += 1
        drop_y = 300
        boat_y = 220

    index = 0
    while index < len(word):
        if word[index].lower() in a:
            b_drop_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + widths[index] // 2 - 63
            bg.paste(b_drop, (b_drop_x, drop_y))
            index += 1
        elif word[index].lower() in b:
            try:
                if word[index + 1].lower() in b:
                    s_drop_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + widths[index] // 2 - 31
                    bg.paste(s_drop, (s_drop_x, drop_y))
                    index += 1
                elif word[index + 1].lower() in a:
                    boat_x = sum(widths[:index]) + 40 * len(widths[:index]) + 20 #s
                    boat_1 = boat.resize((widths[index] + widths[index + 1] + 80, 128))
                    bg.paste(boat_1, (boat_x, boat_y), boat_1)
                    index += 2
                else:
                    s_drop_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + widths[index] // 2 - 31
                    bg.paste(s_drop, (s_drop_x, drop_y))
                    index += 1
            except IndexError:
                s_drop_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + widths[index] // 2 - 31
                bg.paste(s_drop, (s_drop_x, drop_y))
                index += 1
        else:
            index += 1
    return bg, new_line


def word_with_drops(word, is_text):
    width_total = (len(word) - 1) * 40 + 80
    widths = []
    chars = []
    new_line = False
    for char in word:
        try:
            if char == '?':
                img = Image.open('Буквы/q.png')
            elif char == ':':
                img = Image.open('Буквы/colon.png')
            elif char == '"':
                img = Image.open('Буквы/comas.png')
            elif char == '-' or char == '–' or char == '—':
                img = Image.open('Буквы/--scale-4_00x.png')
            else:
                img = Image.open('Буквы/' + char.upper() + '-scale-4_00x.png')
            width, height = img.size
        except:
            pass

        if char == char.upper():
            if char == 'Ё':
                img = img.resize((300 * width // height, 300), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Щ' or char == 'Ц':
                img = img.resize((240 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Й':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == '.':
                img = img.resize((60 * width // height, 60), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == ',':
                img = img.resize((100 * width // height, 100), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '"':
                img = img.resize((100 * width // height, 100), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '!':
                img = img.resize((290 * width // height, 290), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '?':
                img = img.resize((290 * width // height, 290), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '-':
                img = img.resize((150 * width // height, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '–':
                img = img.resize((150 * width // height + 150, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '—':
                img = img.resize((150 * width // height + 200, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == ':':
                img = img.resize((220 * width // height, 220), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == ';':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '*':
                new_line = True
            elif char == '_':
                width_total += 200
                widths.append(200)
                chars.append(Image.new('RGB', (200, 250), 'white'))
            else:
                img = img.resize((240 * width // height, 240), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
        else:
            if char == 'ё':
                img = img.resize((260 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'щ' or char == 'ц':
                img = img.resize((200 * width // height, 220), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'й':
                img = img.resize((230 * width // height, 230), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            else:
                img = img.resize((200 * width // height, 200), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue

    if is_text:
        bg = Image.new('RGB', (width_total, 540), 'white')
        x = 40
        index = 0
        for img in chars:
            if word[index] == 'Ё':
                bg.paste(img, (x, 0))
            elif word[index] == 'ё':
                bg.paste(img, (x, 40))
            elif word[index] == 'Й':
                bg.paste(img, (x, 20))
            elif word[index] == 'й':
                bg.paste(img, (x, 70))
            elif word[index] == '.':
                bg.paste(img, (x, 250))
            elif word[index] == ',':
                bg.paste(img, (x, 270))
            elif word[index] == ',':
                bg.paste(img, (x, 10))
            elif word[index] == '!':
                bg.paste(img, (x, 10))
            elif word[index] == '?':
                bg.paste(img, (x, 10))
            elif word[index] == ':':
                bg.paste(img, (x, 100))
            elif word[index] == ';':
                bg.paste(img, (x, 100))
            elif word[index] == '-' or word[index] == '–' or word[index] == '—':
                bg.paste(img, (x, 150))
            elif word[index] == word[index].upper():
                bg.paste(img, (x, 60))
            elif word[index] == word[index].lower():
                bg.paste(img, (x, 100))
            x += widths[index] + 40
            index += 1
        drop_y = 340
    
    else:
        bg = Image.new('RGB', (width_total, 500), 'white')
        x = 40
        index = 0
        for img in chars:
            if word[index] == 'ё':
                bg.paste(img, (x, 0))
            elif word[index] == 'й':
                bg.paste(img, (x, 30))
            elif word[index].upper() == '.':
                bg.paste(img, (x, 230))
            elif word[index] == ',':
                bg.paste(img, (x, 230))
            elif word[index] == '"':
                bg.paste(img, (x, 10))
            elif word[index] == '!':
                bg.paste(img, (x, 0))
            elif word[index] == '?':
                bg.paste(img, (x, 0))
            elif word[index] == ':':
                bg.paste(img, (x, 60))
            elif word[index] == ';':
                bg.paste(img, (x, 60))
            elif word[index] == '-' or word[index] == '–' or word[index] == '—':
                bg.paste(img, (x, 110))
            else:
                bg.paste(img, (x, 60))
            x += widths[index] + 40
            index += 1
        drop_y = 300
        boat_y = 220

    index = 0
    while index < len(word):
        if word[index].lower() in a:
            b_drop_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + widths[index] // 2 - 63
            bg.paste(b_drop, (b_drop_x, drop_y))
            index += 1
        elif word[index].lower() in b:
            try:
                if word[index + 1].lower() in b:
                    s_drop_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + widths[index] // 2 - 31
                    bg.paste(s_drop, (s_drop_x, drop_y))
                    index += 1
                elif word[index + 1].lower() in a:
                    index += 2
                else:
                    s_drop_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + widths[index] // 2 - 31
                    bg.paste(s_drop, (s_drop_x, drop_y))
                    index += 1
            except IndexError:
                s_drop_x = sum(widths[:index]) + 40 * len(widths[:index]) + 40 + widths[index] // 2 - 31
                bg.paste(s_drop, (s_drop_x, drop_y))
                index += 1
        else:
            index += 1
    return bg, new_line


def word_with_boats(word, is_text):
    width_total = (len(word) - 1) * 40 + 80
    widths = []
    chars = []
    new_line = False
    for char in word:
        try:
            if char == '?':
                img = Image.open('Буквы/q.png')
            elif char == ':':
                img = Image.open('Буквы/colon.png')
            elif char == '"':
                img = Image.open('Буквы/comas.png')
            elif char == '-' or char == '–' or char == '—':
                img = Image.open('Буквы/--scale-4_00x.png')
            else:
                img = Image.open('Буквы/' + char.upper() + '-scale-4_00x.png')
            width, height = img.size
        except:
            pass

        if char == char.upper():
            if char == 'Ё':
                img = img.resize((300 * width // height, 300), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Щ' or char == 'Ц':
                img = img.resize((240 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Й':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == '.':
                img = img.resize((60 * width // height, 60), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == ',':
                img = img.resize((100 * width // height, 100), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '"':
                img = img.resize((100 * width // height, 100), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '!':
                img = img.resize((290 * width // height, 290), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '?':
                img = img.resize((290 * width // height, 290), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '-':
                img = img.resize((150 * width // height, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '–':
                img = img.resize((150 * width // height + 150, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '—':
                img = img.resize((150 * width // height + 200, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == ':':
                img = img.resize((220 * width // height, 220), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == ';':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '*':
                new_line = True
            elif char == '_':
                width_total += 200
                widths.append(200)
                chars.append(Image.new('RGB', (200, 250), 'white'))
            else:
                img = img.resize((240 * width // height, 240), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
        else:
            if char == 'ё':
                img = img.resize((260 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'щ' or char == 'ц':
                img = img.resize((200 * width // height, 220), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'й':
                img = img.resize((230 * width // height, 230), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            else:
                img = img.resize((200 * width // height, 200), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue

    if is_text:
        bg = Image.new('RGB', (width_total, 540), 'white')
        x = 40
        index = 0
        for img in chars:
            if word[index] == 'Ё':
                bg.paste(img, (x, 0))
            elif word[index] == 'ё':
                bg.paste(img, (x, 40))
            elif word[index] == 'Й':
                bg.paste(img, (x, 20))
            elif word[index] == 'й':
                bg.paste(img, (x, 70))
            elif word[index] == '.':
                bg.paste(img, (x, 250))
            elif word[index] == ',':
                bg.paste(img, (x, 270))
            elif word[index] == ',':
                bg.paste(img, (x, 10))
            elif word[index] == '!':
                bg.paste(img, (x, 10))
            elif word[index] == '?':
                bg.paste(img, (x, 10))
            elif word[index] == ':':
                bg.paste(img, (x, 100))
            elif word[index] == ';':
                bg.paste(img, (x, 100))
            elif word[index] == '-' or word[index] == '–' or word[index] == '—':
                bg.paste(img, (x, 150))
            elif word[index] == word[index].upper():
                bg.paste(img, (x, 60))
            elif word[index] == word[index].lower():
                bg.paste(img, (x, 100))
            x += widths[index] + 40
            index += 1
        drop_y = 340
        boat_y = 260
    else:
        bg = Image.new('RGB', (width_total, 500), 'white')
        x = 40
        index = 0
        for img in chars:
            if word[index] == 'ё':
                bg.paste(img, (x, 0))
            elif word[index] == 'й':
                bg.paste(img, (x, 30))
            elif word[index].upper() == '.':
                bg.paste(img, (x, 230))
            elif word[index] == ',':
                bg.paste(img, (x, 230))
            elif word[index] == '"':
                bg.paste(img, (x, 10))
            elif word[index] == '!':
                bg.paste(img, (x, 0))
            elif word[index] == '?':
                bg.paste(img, (x, 0))
            elif word[index] == ':':
                bg.paste(img, (x, 60))
            elif word[index] == ';':
                bg.paste(img, (x, 60))
            elif word[index] == '-' or word[index] == '–' or word[index] == '—':
                bg.paste(img, (x, 110))
            else:
                bg.paste(img, (x, 60))
            x += widths[index] + 40
            index += 1
        drop_y = 300
        boat_y = 220

    index = 0
    while index < len(word):
        if word[index].lower() in a:
            index += 1
        elif word[index].lower() in b:
            try:
                if word[index + 1].lower() in b:
                    index += 1
                elif word[index + 1].lower() in a:
                    boat_x = sum(widths[:index]) + 40 * len(widths[:index]) + 20
                    boat_1 = boat.resize((widths[index] + widths[index + 1] + 80, 128))
                    bg.paste(boat_1, (boat_x, boat_y), boat_1)
                    index += 2
                else:
                    index += 1
            except IndexError:
                index += 1
        else:
            index += 1
    return bg, new_line


def word_only(word, is_text):
    width_total = (len(word) - 1) * 40 + 80
    widths = []
    chars = []
    new_line = False
    for char in word:
        try:
            if char == '?':
                img = Image.open('Буквы/q.png')
            elif char == ':':
                img = Image.open('Буквы/colon.png')
            elif char == '"':
                img = Image.open('Буквы/comas.png')
            elif char == '-' or char == '–' or char == '—':
                img = Image.open('Буквы/--scale-4_00x.png')
            else:
                img = Image.open('Буквы/' + char.upper() + '-scale-4_00x.png')
            width, height = img.size
        except:
            pass

        if char == char.upper():
            if char == 'Ё':
                img = img.resize((300 * width // height, 300), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Щ' or char == 'Ц':
                img = img.resize((240 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'Й':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == '.':
                img = img.resize((60 * width // height, 60), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == ',':
                img = img.resize((100 * width // height, 100), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '"':
                img = img.resize((100 * width // height, 100), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '!':
                img = img.resize((290 * width // height, 290), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '?':
                img = img.resize((290 * width // height, 290), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '-':
                img = img.resize((150 * width // height, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '–':
                img = img.resize((150 * width // height + 150, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '—':
                img = img.resize((150 * width // height + 200, 150), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == ':':
                img = img.resize((220 * width // height, 220), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == ';':
                img = img.resize((280 * width // height, 280), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
            elif char == '*':
                new_line = True
            elif char == '_':
                width_total += 200
                widths.append(200)
                chars.append(Image.new('RGB', (200, 250), 'white'))
            else:
                img = img.resize((240 * width // height, 240), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
        else:
            if char == 'ё':
                img = img.resize((260 * width // height, 260), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'щ' or char == 'ц':
                img = img.resize((200 * width // height, 220), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            elif char == 'й':
                img = img.resize((230 * width // height, 230), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue
            else:
                img = img.resize((200 * width // height, 200), Image.ANTIALIAS)
                width, height = img.size
                width_total += width
                widths.append(width)
                chars.append(img)
                continue

    if is_text:
        bg = Image.new('RGB', (width_total, 400), 'white')
        x = 40
        index = 0
        for img in chars:
            if word[index] == 'Ё':
                bg.paste(img, (x, 0))
            elif word[index] == 'ё':
                bg.paste(img, (x, 40))
            elif word[index] == 'Й':
                bg.paste(img, (x, 20))
            elif word[index] == 'й':
                bg.paste(img, (x, 70))
            elif word[index] == '.':
                bg.paste(img, (x, 250))
            elif word[index] == ',':
                bg.paste(img, (x, 270))
            elif word[index] == ',':
                bg.paste(img, (x, 10))
            elif word[index] == '!':
                bg.paste(img, (x, 10))
            elif word[index] == '?':
                bg.paste(img, (x, 10))
            elif word[index] == ':':
                bg.paste(img, (x, 100))
            elif word[index] == ';':
                bg.paste(img, (x, 100))
            elif word[index] == '-' or word[index] == '–' or word[index] == '—':
                bg.paste(img, (x, 150))
            elif word[index] == word[index].upper():
                bg.paste(img, (x, 60))
            elif word[index] == word[index].lower():
                bg.paste(img, (x, 100))
            x += widths[index] + 40
            index += 1

    else:
        bg = Image.new('RGB', (width_total, 350), 'white')
        x = 40
        index = 0
        for img in chars:
            if word[index] == 'ё':
                bg.paste(img, (x, 0))
            elif word[index] == 'й':
                bg.paste(img, (x, 30))
            elif word[index].upper() == '.':
                bg.paste(img, (x, 230))
            elif word[index] == ',':
                bg.paste(img, (x, 230))
            elif word[index] == '"':
                bg.paste(img, (x, 10))
            elif word[index] == '!':
                bg.paste(img, (x, 0))
            elif word[index] == '?':
                bg.paste(img, (x, 0))
            elif word[index] == ':':
                bg.paste(img, (x, 60))
            elif word[index] == ';':
                bg.paste(img, (x, 60))
            elif word[index] == '-' or word[index] == '–' or word[index] == '—':
                bg.paste(img, (x, 110))
            else:
                bg.paste(img, (x, 60))
            x += widths[index] + 40
            index += 1

    return bg, new_line


def text(text1, size, orientation, mode):
    if orientation == 'альбомная':
        width, height = 3508, 2480
    elif orientation == 'книжная':
        width, height = 2480, 3508

    bg = Image.new('RGB', (width, height), 'white')

    x, y = 100, 100
    text_list = list(text1.replace('\n', '* ').split())
    img_height = 0
    x_max = 0
    while y + img_height + 0.1 * size <= height:
        try:
            w = text_list[0]
        except:
            break
        if mode == 'Обычный':
            img, new_line = word(w, True)
        elif mode == 'Только буквы':
            img, new_line = word_only(w, True)
        elif mode == 'Буквы и капельки':
            img, new_line = word_with_drops(w, True)
        elif mode == 'Буквы и лодочки':
            img, new_line = word_with_boats(w, True)
        
        img_width, img_height = img.size
        img = img.resize((math.ceil(80 * img_width // img_height * (size / 10)), math.ceil(80 * (size / 10))), Image.ANTIALIAS)
        img_width, img_height = img.size
        if x + img_width + 100 <= width:
            bg.paste(img, (math.ceil(x), math.ceil(y)))
            if x + img_width + 100 > x_max:
                x_max = x + img_width
            x += img_width + 2 * size

        else:
            if x > x_max:
                x_max = x
            y += img_height + 0.1 * size
            x = 100
            bg.paste(img, (math.ceil(x), math.ceil(y)))
            x += img_width + 2 * size
        
        if new_line:
            if x > x_max:
                x_max = x
            y += img_height + 0.1 * size
            x = 100
        
        try:
            del text_list[0]
        except:
            break
    if x_max > width:
        x_max = width
    if y + 50 + img_height > height:
        y = height
    else:
        y = y + 50 + img_height
    bg = bg.crop((0, 0, x_max + 100, y))
    if len(text_list) != 0:
        text1 = ' '.join(text_list)
        return bg, text1
    return bg, ''