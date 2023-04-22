# https://www.beecrowd.com.br/judge/pt/problems/view/1140

while True:
    sentence = input().lower().split()
    if sentence[0] == '*':
        break

    initialLetter = sentence[0][0]
    for word in sentence:
        if word[0] != initialLetter:
            print('N')
            break
    
    else:
        print('Y')
