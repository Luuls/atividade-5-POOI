# https://www.beecrowd.com.br/judge/pt/problems/view/2453

encodedSentence = input()

decodedSentence = ''
for word in encodedSentence.split():
    for i in range(1, len(word), 2):
        decodedSentence += word[i]

    decodedSentence += ' '
    
print(decodedSentence[0:-1])