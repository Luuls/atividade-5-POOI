# https://www.beecrowd.com.br/judge/pt/homeworks/view/31675

mapForPassword =    [ 
                      'GQaku',
                      'ISblv',
                      'EOYcmw',
                      'FPZdnx',
                      'JTeoy',
                      'DNXfpz',
                      'AKUgq',
                      'CMWhr',
                      'BLVis',
                      'HRjt'
                    ]

n = int(input())

for _ in range(n):
    password = input().replace(' ', '')[0 : 12]

    newPassword = ''
    for letter in password:
        for i, key in enumerate(mapForPassword):
            if letter in key:
                newPassword += str(i)
    print(newPassword)
    