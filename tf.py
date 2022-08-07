def printer(a,b,c,d,e,f,g,h,i):
    print(a + "|" + b + "|" + c )
    print("______")
    print(d + "|" + e + "|" + f )
    print("______")
    print(g + "|" + h + "|" + i )
def pfx(z, ol, xl):
    l=[1,2,3,4,5,6,7,8,9]
    l[z-1]='x'
    rx=[]
    for i in ol:
        l[i-1] = 'o'
    for j in xl:
        l[j-1] = 'x'
    for d in range(9):
        t=str(l[d])
        rx.append(t)
    printer(rx[0],rx[1],rx[2],rx[3],rx[4],rx[5],rx[6],rx[7],rx[8])
def pfo(k,ol,xl):
    w=[1,2,3,4,5,6,7,8,9]
    w[k-1]='o'
    ro=[]
    for i in ol:
        w[i-1] = 'o'
    for j in xl:
        w[j-1] = 'x'
    for i in range(9):
        k=str(w[i])
        ro.append(k)
    printer(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8])

    
