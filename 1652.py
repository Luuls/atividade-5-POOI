# https://www.beecrowd.com.br/judge/pt/problems/view/1652

consonants = 'bcdfghjklmnpqrstvwxyz'
endConstraints1 = ['o', 's', 'x'] 
endConstraints2 = ['ch', 'sh']

l, n = map(int, input().split())

irregularWords = {}
for _ in range(l):
    singular, plural = input().split()
    irregularWords[singular] = plural

for _ in range(n):
    word = input()
    
    if word in irregularWords:
        print(irregularWords[word])

    elif word[-2] in consonants and word[-1] == 'y':
        print(word[:-1] + 'ies')

    elif word[-1] in endConstraints1 or word[-2:] in endConstraints2:
        print(word + 'es')

    else:
        print(word + 's')