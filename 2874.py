# https://www.beecrowd.com.br/judge/pt/problems/view/2874

while True:
    try:
        n = int(input())

    except EOFError:
        break

    message = ''
    for _ in range(n):
        byteString = input()
    
        letter = chr(int(byteString, 2))
        message += letter

    print(message)