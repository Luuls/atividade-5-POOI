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

middleLayer = \
'''\
|   |                                    |   |\n|   |                                    |   |\
'''

bottomLayer = \
'''\
|   |                                    |   |
|   |   32    16    8     4     2     1  |   |_
|   |____________________________________|   |_)
|                                            |
|____________________________________________|\n\
'''

hoursLayerPlaceholder = \
'''\
|   |   {}         {}         {}         {}  |   |\
'''

minutesLayerPlaceholder = \
'''\
|   |   {}     {}     {}     {}     {}     {}  |   |\
'''
while True:
    try:
        hours, minutes = input().split(':')

    except EOFError:
        break
    
    hoursBin = f'{int(hours):04b}'
    minutesBin = f'{int(minutes):06b}'

    hoursPlaceholder = hoursLayerPlaceholder.index('{}')
    minutesPlaceholder = minutesLayerPlaceholder.index('{}')

    hoursLayerPlaceholderCopy = hoursLayerPlaceholder
    minutesLayerPlaceholderCopy = minutesLayerPlaceholder
    
    hoursLayerPlaceholderCopy = hoursLayerPlaceholderCopy.format(\
            'o' if hoursBin[0] == '1' else ' ',
            'o' if hoursBin[1] == '1' else ' ',
            'o' if hoursBin[2] == '1' else ' ',
            'o' if hoursBin[3] == '1' else ' '
            )
    
    minutesLayerPlaceholderCopy = minutesLayerPlaceholderCopy.format(\
            'o' if minutesBin[0] == '1' else ' ',
            'o' if minutesBin[1] == '1' else ' ',
            'o' if minutesBin[2] == '1' else ' ',
            'o' if minutesBin[3] == '1' else ' ',
            'o' if minutesBin[4] == '1' else ' ',
            'o' if minutesBin[5] == '1' else ' '
            )

    print(topLayer)
    print(hoursLayerPlaceholderCopy)
    print(middleLayer)
    print(minutesLayerPlaceholderCopy)
    print(bottomLayer)