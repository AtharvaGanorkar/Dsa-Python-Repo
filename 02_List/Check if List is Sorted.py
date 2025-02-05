l = [int(x) for x in input("Enter numbers Seperated by commas: ").split(',')]
#l=[]
def CheckSorted(l):
    Slist = sorted(l)
    if Slist == l or not l :
        return True
    else:
        return False

print(CheckSorted(l))


def isSorted(l):
    i = 1
    for i in range(len(l)):
        if l[i] < l[i-1]:
            return False
        i =+1
    return True

l = [10,20,30,15,40]
print(isSorted(l))
   