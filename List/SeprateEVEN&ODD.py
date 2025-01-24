N = input("Enter Numbers Separted by commas: ").split(',')
N = [int(x) for x in N]

def EVENODD(N):
    EVEN=[]
    ODD=[]
    for x in N:
        if x % 2 == 0:
            EVEN.append(x)
        else:
            ODD.append(x)
    print("Even Numbers:", EVEN)
    print("Odd Numbers:", ODD)

EVENODD(N)
       