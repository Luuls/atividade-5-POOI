# https://www.beecrowd.com.br/judge/pt/problems/view/2304

def buy(player, value):
    players[player] -= value
    return

def sell(player, value):
    players[player] += value
    return

operations = {'V': sell, 'C': buy}

i, n = map(int, input().split())
players = {p: i for p in 'DEF'}
for _ in range(n):
    gameRoundLog = input().split()

    if len(gameRoundLog) > 3:
        _, receiver, payer, value = gameRoundLog
        value = int(value)

        players[receiver] += value
        players[payer] -= value
    
    else:
        operation, player, value = gameRoundLog
        value = int(value)
        
        operations[operation](player, value)

print(*players.values())
