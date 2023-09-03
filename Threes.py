#score
def fscore(table):
    score = 0
    for i in table:
        for j in range(4):
            temp_score = 0
            if i[j]%3 == 0 and i[j] != 0:
                temp_score += 1
                TI = i[j]//3
                TS = 1
                while TI != 1:
                    TI = TI//2
                    TS += 1
                for k in range(TS):
                    temp_score = temp_score*3
            score += temp_score
    return score
#-----------
White = (6, 23, 21)
Black = (13,47,44)
Red = (66,190,178)
Blue = (199,253,248)
import pygame
import sys
pygame.init()
font = pygame.font.SysFont("Times new Roman",75)
pygame.display.set_caption("Threes				             		             Pedy The hansi  ")
surface = pygame.display.set_mode((800,920))
surface.fill(White)
Stable = pygame.Rect(30,30,740,740)
pygame.draw.rect(surface,Red,Stable,0,30)
#row 1
Stable = pygame.Rect(60,60,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(235,60,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(410,60,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(585,60,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
#row 2
Stable = pygame.Rect(60,235,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(235,235,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(410,235,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(585,235,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
#row 3
Stable = pygame.Rect(60,410,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(235,410,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(410,410,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(585,410,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
#row 4
Stable = pygame.Rect(60,585,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(235,585,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(410,585,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(585,585,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
pygame.display.flip( )
##LI
import random
## table check
def TC(x):
    tc = []
    for i in range(len(x)):
        for j in range(len(x)):
            tc += [x[i][j]]
    return tc
def check(x,tc):
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i][j] != tc[(i*4)+j]:
                return True
    return False
##move right & left
def right(y):
    x = y[:]
    for i in range(len(x)):
        for j in range(len(x)-2,-1,-1):
            if x[i][j] == 0 or x[i][j+1]== x[i][j] == 2 or x[i][j+1] == x[i][j] == 1 :
                continue
            if x[i][j+1] == 0:
                x[i][j+1] = x[i][j]
                x[i][j] = 0
            elif x[i][j+1] == x[i][j] or x[i][j] + x[i][j+1] == 3:
                x[i][j+1] = x[i][j] + x[i][j+1]
                x[i][j] = 0
    return x
def left(y):
    x = y[:]
    for i in range(len(x)):
        x[i] = x[i][::-1]
    x = right(x)
    for i in range(len(x)):
        x[i] = x[i][::-1]
    return x
##move up & down
def up(y):
    x = y[:]
    for i in range(len(x)):
        for j in range(1,len(x)):
            if x[j][i] == 0 or x[j-1][i] == x[j][i] == 2 or x[j-1][i] == x[j][i] == 1:
                continue
            if x[j-1][i] == 0:
                x[j-1][i] = x[j][i]
                x[j][i] = 0
            elif x[j-1][i] == x[j][i] or x[j-1][i]+x[j][i] == 3:
                x[j-1][i] += x[j][i]
                x[j][i] = 0
    return x
def down(y):
    x = y[:]
    x = x[::-1]
    x = up(x)
    x = x[::-1]
    return x
##add new number
def NewNumber(x,d,k,tt):
    m = 0
    Z = -1
    if tt == 'D':
        for i in range(len(x)):
             if x[0][i] == 0:
                 m +=1
        for j in range(len(x)):
                if x[0][j] == 0:
                    Z += 1
                    if Z == k%m:
                        x[0][j] = d
                        return x
    elif tt == 'U':
        for i in range(len(x)):
             if x[len(x)-1][i] == 0:
                 m +=1
        for j in range(len(x)):
            if x[len(x)-1][j] == 0:
                Z += 1
                if Z == k%m:
                    x[len(x)-1][j] = d
                    return x
    elif tt == 'R':
        for i in range(len(x)):
            if x[i][0] == 0:
                m += 1
        for j in range(len(x)):
            if x[j][0] == 0:
                Z += 1
                if Z == k%m:
                    x[j][0] = d
                    return x
    elif tt == 'L':
        for i in range(len(x)):
            if x[i][len(x)-1] == 0:
                m += 1
        for j in range(len(x)):
            if x[j][len(x)-1] == 0:
                Z += 1
                if Z == k%m:
                    x[j][len(x)-1] = d
                    return(x)
    return x
##Table
table = [[0]*4 for i in range(4)]
for i in range(9):
    r,c = random.randint(0,3), random.randint(0,3)
    while table[r][c]!=0:
        r,c = random.randint(0,3), random.randint(0,3)
    table[r][c] = random.randint(1,3)
##move command
table_chek = TC(table)
TT = ''
flag = False
d = random.randint(1,3)
while True:
    Check = check(table,table_chek)
    if Check:
        table = NewNumber(table,d,random.randint(1,4),TT)
        table_chek = TC(table)
        d = random.randint(1,3)
        #row 1
        Stable = pygame.Rect(60,60,150,150)
        pygame.draw.rect(surface,Blue,Stable,0,30)
        Stable = pygame.Rect(235,60,150,150)
        pygame.draw.rect(surface,Blue,Stable,0,30)
        Stable = pygame.Rect(410,60,150,150)
        pygame.draw.rect(surface,Blue,Stable,0,30)
        Stable = pygame.Rect(585,60,150,150)
        pygame.draw.rect(surface,Blue,Stable,0,30)
        #row 2
        Stable = pygame.Rect(60,235,150,150)
        pygame.draw.rect(surface,Blue,Stable,0,30)
        Stable = pygame.Rect(235,235,150,150)
        pygame.draw.rect(surface,Blue,Stable,0,30)
        Stable = pygame.Rect(410,235,150,150)
        pygame.draw.rect(surface,Blue,Stable,0,30)
        Stable = pygame.Rect(585,235,150,150)
        pygame.draw.rect(surface,Blue,Stable,0,30)
        #row 3
        Stable = pygame.Rect(60,410,150,150)
        pygame.draw.rect(surface,Blue,Stable,0,30)
        Stable = pygame.Rect(235,410,150,150)
        pygame.draw.rect(surface,Blue,Stable,0,30)
        Stable = pygame.Rect(410,410,150,150)
        pygame.draw.rect(surface,Blue,Stable,0,30)
        Stable = pygame.Rect(585,410,150,150)
        pygame.draw.rect(surface,Blue,Stable,0,30)
        #row 4
        Stable = pygame.Rect(60,585,150,150)
        pygame.draw.rect(surface,Blue,Stable,0,30)
        Stable = pygame.Rect(235,585,150,150)
        pygame.draw.rect(surface,Blue,Stable,0,30)
        Stable = pygame.Rect(410,585,150,150)
        pygame.draw.rect(surface,Blue,Stable,0,30)
        Stable = pygame.Rect(585,585,150,150)
        pygame.draw.rect(surface,Blue,Stable,0,30)
        pygame.display.flip( )
    else:
        checking = []
        for W in range(4):
            A = []
            for Q in range(4):
                    A += [table_chek[Q*4:(Q+1)*4]]
            if W == 0:
                checking += [(left(A))]
            elif W == 1:
                checking += [(down(A))]
            elif W == 2:
                checking += [(right(A))]
            elif W == 3:
                checking += [(up(A))]
        if checking[0]==checking[1]==checking[2]==checking[3]==table:
            flag = True
            break
    if flag:
        break
    for i in range(4):
        XY = 115
        for j in range(4):
            ttext = str(table[i][j])
            font_name , font_size = "Arial" , 80
            color = (0,0,0)
            if table[i][j] == 1:
                color = (20,190,88)
            if table[i][j] == 2:
                color = (22,101,190)
            if table[i][j] == 0:
                ttext = ''
            text = font.render(ttext,True,color)
            XY = 115
            if table[i][j] > 10:
                XY = 95
            elif table[i][j] > 100:
                XY = 75
            surface.blit(text,(XY + j*(175),95+i*(175)))
    Stable = pygame.Rect(0,800,800,120)
    pygame.draw.rect(surface,White,Stable)
    Stable = pygame.Rect(205,780,125,125)
    pygame.draw.rect(surface,Blue,Stable,0,30)
    color = (0,0,0)
    if d == 1:
        color = (20,190,88)
    if d == 2:
        color = (22,101,190)
    text = font.render(str(d),True,color)
    surface.blit(text,(250,800))
    SCORE = fscore(table)
    text = font.render("score : "+str(SCORE),True,Blue)
    surface.blit(text,(400,800))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if  event.key== pygame.K_UP :
                TT = 'U'
                table = up(table)
                break
            elif  event.key== pygame.K_RIGHT :
                TT = 'R'
                table = right(table)
                break
            elif event.key== pygame.K_LEFT :
                TT = 'L'
                table = left(table)
                break
            elif  event.key == pygame.K_DOWN :
                TT = 'D'
                table = down(table)
                break
            elif event.key == pygame.K_ESCAPE:
                flag = True
                break
    if flag:
        break
table = NewNumber(table,random.randint(1,3),random.randint(1,4),TT)
##print table and score
#row 1
Stable = pygame.Rect(60,60,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(235,60,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(410,60,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(585,60,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
#row 2
Stable = pygame.Rect(60,235,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(235,235,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(410,235,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(585,235,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
#row 3
Stable = pygame.Rect(60,410,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(235,410,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(410,410,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(585,410,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
#row 4
Stable = pygame.Rect(60,585,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(235,585,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(410,585,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
Stable = pygame.Rect(585,585,150,150)
pygame.draw.rect(surface,Blue,Stable,0,30)
pygame.display.flip( )
for i in range(4):
    XY = 115
    for j in range(4):
        ttext = str(table[i][j])
        font_name , font_size = "Arial" , 80
        color = (0,0,0)
        if table[i][j] == 1:
            color = (20,190,88)
        if table[i][j] == 2:
            color = (22,101,190)
        if table[i][j] == 0:
            ttext = ''
        text = font.render(ttext,True,color)
        XY = 115
        if table[i][j] > 10:
            XY = 95
        elif table[i][j] > 100:
            XY = 75
        surface.blit(text,(XY + j*(175),95+i*(175)))
        pygame.display.flip()
score = 0
for i in table:
    for j in range(4):
        temp_score = 0
        if i[j]%3 == 0 and i[j] != 0:
            temp_score += 1
            TI = i[j]//3
            TS = 1
            while TI != 1:
                TI = TI//2
                TS += 1
            for k in range(TS):
                temp_score = temp_score*3
        score += temp_score
if TC(right(table[:]))==TC(table) and TC(left(table[:]))==TC(table) and TC(down(table[:]))==TC(table) and TC(up(table[:]))==TC(table):
    Stable = pygame.Rect(50,770,700,150)
    pygame.draw.rect(surface,White,Stable)
    Stable = pygame.Rect(50,800,700,100)
    pygame.draw.rect(surface,Black,Stable,0,40)
    text = font.render('The final score is '+str(score)+'.',True,Blue)
    surface.blit(text,(60,810))
    pygame.display.flip()
else:
    Stable = pygame.Rect(50,770,700,150)
    pygame.draw.rect(surface,White,Stable)
    Stable = pygame.Rect(50,800,700,100)
    pygame.draw.rect(surface,Black,Stable,0,40)
    text = font.render('The partial score is '+str(score)+'.',True,Blue)
    surface.blit(text,(60,810))
    pygame.display.flip()
while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key== pygame.K_ESCAPE):
            exit(0)