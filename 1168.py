# https://www.beecrowd.com.br/judge/pt/problems/view/1168

ledsAmounts = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6] #quantidade necessária para cada indice (digito)
n = int(input())

for _ in range(n):
    leds = 0
    number = input()
    for digit in number:
        leds += ledsAmounts[int(digit)]
    
    print(leds, 'leds')