# https://www.beecrowd.com.br/judge/pt/problems/view/2457

letterToSearch = input()
sentence = input().split()

wordsContainingTheLetter = 0
for word in sentence:
    if letterToSearch in word:
        wordsContainingTheLetter += 1

percentage = 100 * wordsContainingTheLetter / len(sentence)
print(f'{percentage:.1f}')