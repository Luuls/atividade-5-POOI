# https://www.beecrowd.com.br/judge/pt/problems/view/1561

topLayer = \
'''\
 ____________________________________________
|                                            |
|    ____________________________________    |_
|   |                                    |   |_)
|   |   8         4         2         1  |   |
|   |                                    |   |\
'''

hoursLayerPlaceholder = \
'''\
|   |   {}         {}         {}         {}  |   |\
'''

middleLayer = \
'''\
|   |                                    |   |\n|   |                                    |   |\
'''

minutesLayerPlaceholder = \
'''\
|   |   {}     {}     {}     {}     {}     {}  |   |\
'''

bottomLayer = \
'''\
|   |                                    |   |
|   |   32    16    8     4     2     1  |   |_
|   |____________________________________|   |_)
|                                            |
|____________________________________________|\n\
'''


while True:
    try:
        hours, minutes = input().split(':')

    except EOFError:
        break
    
    hoursBin = f'{int(hours):04b}'
    minutesBin = f'{int(minutes):06b}'

    hoursLayerPlaceholderCopy = hoursLayerPlaceholder
    minutesLayerPlaceholderCopy = minutesLayerPlaceholder
    
    hoursLayerPlaceholderCopy = hoursLayerPlaceholderCopy.format(\
            *['o' if bit == '1' else ' ' for bit in hoursBin] 
            )
    
    minutesLayerPlaceholderCopy = minutesLayerPlaceholderCopy.format(\
            *['o' if bit == '1' else ' ' for bit in minutesBin]
            )

    print(topLayer)
    print(hoursLayerPlaceholderCopy)
    print(middleLayer)
    print(minutesLayerPlaceholderCopy)
    print(bottomLayer)
