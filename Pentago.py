game,H,count,flag,flag2 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],'',1,True,False
player1 = input('player 1 :   ')
player2 = input('player 2 :   ')
def Change_MapL(x):
    for i in range(3):
        for j in range(3):
            if i + j < 3:
                temp = x[i+j][i]
                x[i+j][i] = x[i][i+j]
                x[i][i+j] = temp
    x = x[::-1]
    return x
def Change_MapR(x):
    for M in range(3):
        for i in range(3):
            for j in range(3):
                if i + j < 3:
                    temp = x[i+j][i]
                    x[i+j][i] = x[i][i+j]
                    x[i][i+j] = temp
        x = x[::-1]
    return x
while flag and count < 37:
    if H != 'map 1':
        map1 = [game[0][:3],game[1][:3],game[2][:3]]
    if H != 'map 2':
        map2 = [game[0][3:6],game[1][3:6],game[2][3:6]]
    if H != 'map 3':
        map3 = [game[3][:3],game[4][:3],game[5][:3]]
    if H != 'map 4':
        map4 = [game[3][3:6],game[4][3:6],game[5][3:6]]
    game = [map1[0]+map2[0],map1[1]+map2[1],map1[2]+map2[2],map3[0]+map4[0],map3[1]+map4[1],map3[2]+map4[2]]
    for Z in range(6):
        W = game[Z]
        string = ''
        for P in range(6):
            if W[P] == 2:
                string += 'B  '
            elif W[P] == 3:
                string += 'W  '
            else:
                string += 'O  '
            if P == 2:
                string += '|  '
        print(' '+string+' ')
        if Z == 2:
            print('---------------------------------')
    H = ''
    print()
    print('Place!')
    while True:
        if count % 2 == 0:
            print(player2+"'s Turn")
        else:
            print(player1+"'s Turn")
        c = input().split()
        a = int(c[0]) - 1
        b = int(c[1]) - 1
        if game[b][a] == 0:
            if count % 2 == 0:
                game[b][a] = 2
            else:
                game[b][a] = 3
            break
        else:
            print("You cant Place Here!")
    if H != 'map 1':
        map1 = [game[0][:3],game[1][:3],game[2][:3]]
    if H != 'map 2':
        map2 = [game[0][3:6],game[1][3:6],game[2][3:6]]
    if H != 'map 3':
        map3 = [game[3][:3],game[4][:3],game[5][:3]]
    if H != 'map 4':
        map4 = [game[3][3:6],game[4][3:6],game[5][3:6]]
    while True:
        print('choose map!')
        print('map 1 | map 2\nmap 3 | map 4')
        H = input()
        print('which way to turn?')
        jahat = input()
        if H == 'map 1':
            if jahat == 'left':
                map1 = Change_MapL(map1)
                break
            elif jahat == 'right':
                map1 = Change_MapR(map1)
                break
        elif H == 'map 2':
            if jahat == 'left':
                map2 = Change_MapL(map2)
                break
            elif jahat == 'right':
                map2 = Change_MapR(map2)
                break
        elif H == 'map 3':
            if jahat == 'left':
                map3 = Change_MapL(map3)
                break
            elif jahat == 'right':
                map3 = Change_MapR(map3)
                break
        elif H == 'map 4' :
            if jahat == 'left':
                map4 = Change_MapL(map4)
                break
            elif jahat == 'right':
                map4 = Change_MapR(map4)
                break
    count += 1
    for i in range(6):
        for j in range(6):
            A = B = D = R = 1
            for k in range(5):
                if i+5 <= 6 and j+5 <= 6:
                    A = A*(game[i+k][j+k])
                if i+5 <= 6 and j-5 >= 0:
                    B = B*(game[i+k][j-k])
                if i+5 <= 6:
                    D = D*(game[i+k][j])
                if j+5 <= 6:
                    R = R*(game[i][j+k])
            if A == 32 or B == 32 or D == 32 or R==32:
                print(player2+' wins!')
                flag = False
                flag2 = True
                break
            if A == 243  or B == 243 or D == 243 or R == 243:
                print(player1+' wins!')
                flag = False
                flag2 = True
                break
        if flag2:
            break