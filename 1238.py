# https://www.beecrowd.com.br/judge/pt/problems/view/1238

n = int(input())

for _ in range(n):
    str1, str2 = input().split()

    combinedString = ''
    for letter1, letter2 in zip(str1, str2):
        combinedString += letter1 + letter2

    minLen = min(len(str1), len(str2))

    combinedString += str1[minLen:] + str2[minLen:]
    
    print(combinedString)