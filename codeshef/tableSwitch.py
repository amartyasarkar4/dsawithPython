# cook your dish here
ni = int(input())
for i in range(ni):
    ch = str(input())
    if ch == 'B' or ch == 'b':
        print('BattleShip')
    elif ch == 'C' or ch == 'c':
        print('Cruiser')
    elif ch == 'D' or ch == 'd':
        print('Destroyer')
    elif ch == 'F' or ch == 'f':
        print('Frigate')

    # switch ch:
    #     case 1:
    #         print('BattleShip')
    #         break
    #     case 'C' or 'c':
    #         print('Cruiser')
    #         break
    #     case 'D' or 'd':
    #         print('Destroyer')
    #         break
    #     case 'F' or 'f':
    #         print('Frigate')
    #         break
    #     default:
    #         print('None')
