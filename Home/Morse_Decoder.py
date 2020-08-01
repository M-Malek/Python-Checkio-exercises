MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code):
    words_list = code.split(" ")
    decode_letters = []
    meaning = ""
    j = 0
    for i in words_list:
        if i == '':
            decode_letters.append(" ")
        elif i not in MORSE:
            pass
        else:
            decode_letters.append(MORSE[str(i)])

    while j < len(decode_letters):
        if j == 0:
            meaning += decode_letters[0].upper()
            j += 1
        if decode_letters[j] == ' ' and decode_letters[j+1] == ' ':
            pass
        elif decode_letters[j] == ' ':
            meaning += " "
        else:
            meaning += decode_letters[j]
        j += 1

    return meaning


def splited_input(spl):
    return spl.split(" ")

# word.capitalize() - pierwsza litera tego ciagu znakow (string) zostanie zamieniona na duza litere
code = "... --- -- .   - . -..- -"

#print(splited_input(code))
print(morse_decoder(code))