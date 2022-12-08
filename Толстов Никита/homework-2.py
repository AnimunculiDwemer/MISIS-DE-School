def paintField(a):
    print('--------')
    for i in range(3):
        print('|',end='')
        for j in range(3):
            print(a[i][j],end=' ')
        print('|')
    print('--------')


def isFinish(dls,cell):
    comb=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for i in range(len(comb)):
        if (comb[i][0] in dls[cell]) and (comb[i][1] in dls[cell]) and (comb[i][2] in dls[cell]):
            return True
    return False


print("Play? 1 - yes, 0 - no")
play=int(input())
history=[]
while play==1:
    field =[['-','-','-'],['-','-','-'],['-','-','-']]
    fantomField=[[1,2,3],[4,5,6,],[7,8,9]]
    dls={'X':[],'O':[]}
    paintField(field)
    end=False
    cell='X'
    history.append('Start Game')
    while not end:
        print("Put {0} in cell x,y".format(cell))
        try:
            x=int(input())
            y=int(input())
            field[x][y]
        except:
            print("Цифры от 0 до 2")
            continue
        if field[x][y]!='-':
            print('Close cell')
            continue
        history.append(cell+':'+str(x)+' '+str(y))
        field[x][y]=cell
        dls[cell].append(fantomField[x][y])
        paintField(field)
        if isFinish(dls,cell):
           end=True
           history.append('Win'+cell)
           print('Win '+cell)
        elif (len(dls['X'])+len(dls['O']))==9:
            print('Draw')
            history.append('Draw')
            end=True
        
        if cell=='X':
            cell='O'
        else:
            cell='X'
    
    print("Play? 1 - yes, 0 - no") 
    play=int(input())
file = open('history.txt','w')
for i in history:
    file.write(f'{i}\n')
file.close()
print(history)  
