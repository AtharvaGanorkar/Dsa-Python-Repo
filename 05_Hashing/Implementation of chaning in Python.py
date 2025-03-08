class Chaining:
    def __init__(self,b):
        self.BUCKET = b
        self.table = [[] for i in range(b)]

    def insert(self, e):
        index = e % self.BUCKET
        self.table[index].append(e)
        return self.table

    def remove(self, e):
        index = e % self.BUCKET
        if e in self.table[index]:
            self.table[index].remove(e)
            return self.table
    
    def search(self,e):
        index = e % self.BUCKET
        return e in self.table[index]
        
    

h = Chaining(7)
(h.insert(2))
(h.insert(5))
print(h.insert(2))
print(h.remove(2))
    

