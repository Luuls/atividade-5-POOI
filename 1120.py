# https://www.beecrowd.com.br/judge/pt/problems/view/1120

d, n = input().split()

while d != '0' or n != '0':
    n = n.replace(d, '')
    n = n.lstrip('0')
    
    if n == '':
        n = '0'
    
    print(n)

    d, n = input().split()