'''class Hash:
    def __init__(self,B):
        self.BUCKET = B
        self.Table = [[] for i in range(B)]

    def Insert(self,n):
        index = n % self.BUCKET
        self.Table[index].append(n)
        return self.Table
    
    def Search(self,n):
        index = n % self.BUCKET
        return n in self.Table[index]
        
    def Remove(self,n):
        index = n % self.BUCKET
        if n in self.Table[index]:
            self.Table[index].remove(n)
            return self.Table
        

h = Hash(7)
(h.Insert(2))
(h.Insert(5))
print(h.Insert(2))
print(h.Insert(5))
print(h.Remove(2))'''





