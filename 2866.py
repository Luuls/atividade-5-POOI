# https://www.beecrowd.com.br/judge/pt/problems/view/2866

c = int(input())

for _ in range(c):
    encodedMessage = input()

    message = ''
    for letter in reversed(encodedMessage):
        if letter.islower():
            message += letter

    print(message)