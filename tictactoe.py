import tf
import wincheck
import exc
print('Welcome to the Game, Please note that, Player 1 will be "o" and Player 2 will be "x"')
n1=input("Enter name of Player 1 : " )
n2=input("Enter name of Player 2 : " )
h=0
cl=[]
ol=[]
xl=[]
while True:

    inp=input(n1 + ' Choose from 1 to 9 inclusive both where you want to draw : ' )
    b=exc.excp(inp,n1)

    while True:
        if not b in cl:
            break
        else:
            print("ERROR : You can not choose the same place twice")
            inp=input(n1 + ' Choose from 1 to 9 inclusive both where you want to draw : ' )
            b=exc.excp(inp,n1)
            

    tf.pfo(b,ol,xl)
    cl.append(b)
    ol.append(b)
    h=h+1
    if h>=5:
        if wincheck.wc(ol):
            print(n1 + " won the game. ")
            input("Press Enter to exit the game")
            exit()

    if h>=9:
        print("Game Draw No One Won")
        input("Press Enter to exit the game")
        exit()
    inp=input(n2 + ' Choose from 1 to 9 inclusive both where you want to draw : ' )
    b=exc.excp(inp,n2)
    
    while True:
        if not b in cl:
            break
        else:
            print("ERROR : You can not choose the same place twice")
            inp=input(n1 + ' Choose from 1 to 9 inclusive both where you want to draw : ' )
            b=exc.excp(inp,n2)

    tf.pfx(b,ol,xl)
    
    cl.append(b)
    xl.append(b)
    h=h+1
    if h>=6:
        if wincheck.wc(ol):
            print(n1 + " won the game. ")
            input("Press Enter to exit the game")
            exit()
