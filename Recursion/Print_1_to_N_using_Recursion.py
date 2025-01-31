def OneToN(n):
    if n <= 0:
        return
    OneToN(n-1)
    print(n)

OneToN(4)

class Solution:    
    #Complete this function
    def printNos(self,n):
        if n == 0:
            return
        self.printNos(n-1)
        print(n,end=' ')