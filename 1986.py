# https://www.beecrowd.com.br/judge/pt/problems/view/1986

n = int(input())

encodedMessage = input().split()

message = ''
for code in encodedMessage:
    message += chr(int(code, 16))

print(message)
