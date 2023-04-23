# https://www.beecrowd.com.br/judge/pt/problems/view/2813

n = int(input())

umbrellasHome, umbrellasJob = 0, 0
needInHome, needInJob = 0, 0
for _ in range(n):
    forecastHome, forecastJob = input().split()

    if forecastHome == 'chuva':
        if umbrellasHome == 0:
            needInHome += 1
            
        else: 
            umbrellasHome -= 1

        umbrellasJob += 1

    if forecastJob == 'chuva':
        if umbrellasJob == 0:
            needInJob += 1

        else:
            umbrellasJob -= 1
         
        umbrellasHome += 1

print(needInHome, needInJob)