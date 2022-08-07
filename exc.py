
def excp(n, n3):
    try:
        p = int(n)
        pass
    except:
        print("ERROR : Please enter Integer only from 1 to 9, Entering any thing else will result in error")
        while True:
            inp1=input(n3 + ' Choose from 1 to 9 inclusive both where you want to draw : ' )
            try:
                p = int(inp1)
            except:
                print("ERROR : Please enter Integer only from 1 to 9, Entering any thing else will result in error")
                continue
            if p>= 1 and p <=9:
                return p
            else:
                print("ERROR : Please enter Integer only from 1 to 9, Entering any thing else will result in error")
                continue
    if p>= 1 and p <=9:
        return p
    else:
        print("ERROR : Please enter Integer only from 1 to 9, Entering any thing else will result in error")
        while True:
            inp1=input(n3 + ' Choose from 1 to 9 inclusive both where you want to draw : ' )
            try:
                p = int(inp1)
            except:
                print("ERROR : Please enter Integer only from 1 to 9, Entering any thing else will result in error")
                continue
            if p>= 1 and p <=9:
                return p
            else:
                print("ERROR : Please enter Integer only from 1 to 9, Entering any thing else will result in error")
                continue
        