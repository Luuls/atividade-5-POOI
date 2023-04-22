# https://www.beecrowd.com.br/judge/pt/problems/view/1196

keyboard = '`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./'

while True:
    try:
        sentence = input()

    except EOFError:
        break

    fixedSentence = ''

    for letter in sentence:
        if letter != ' ':
            letterIndex = keyboard.index(letter)
            fixedSentence += keyboard[letterIndex - 1]
        
        else:
            fixedSentence += letter

    print(fixedSentence)