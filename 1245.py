# https://www.beecrowd.com.br/judge/pt/problems/view/1245

while True:
    try:
        n = int(input())
    
    except EOFError:
        break
    
    leftBoots = [0] * 31
    rightBoots = [0] * 31

    pairs = 0

    for _ in range(n):
        m, l = input().split()
        sizeIndex = int(m) - 30
        if l == 'E':
            leftBoots[sizeIndex] += 1
        
        else:
            rightBoots[sizeIndex] += 1

        if leftBoots[sizeIndex] > 0 and rightBoots[sizeIndex] > 0:
            pairs += 1
            leftBoots[sizeIndex] -= 1
            rightBoots[sizeIndex] -= 1

    print(pairs)
