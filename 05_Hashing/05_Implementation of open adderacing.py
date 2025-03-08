class Myhash:
    def __init__(self,n):
        self.Bucket = n
        self.table = [-1 for i in range(n)]

    def insert(self,d):
        index = d % self.Bucket
        if self.table[index] == -1:
            self.table[index] = d

        else:
            k = d % self.Bucket
            flag = 0
            counter = 0

            while counter < self.Bucket and self.table[k] != -1:
                if self.table[k] == d:
                    flag = 1
                    break
                k = (k + 1)%self.Bucket
                counter +=1
            
            if flag != 1:
                if counter < self.Bucket:
                    self.table[k] = d 
        return self.table
    
    
      

    def remove(self,d):
        index = d % self.Bucket
        counter = index
        while self.table[index] != -1:
            if self.table[index] == d:
                self.table[index] = -2
                return True
            index = (index + 1)% self.Bucket    
            if counter == index:
                return False
        return False
          

    def search(self,d):
        index = d % self.Bucket
        counter = index
        while self.table[index] != -1:
            if self.table[index] == d:
                return True
            
            index = (index + 1)% self.Bucket
            if counter == index:
                return False
        return False


    
h = Myhash(7)
print(h.insert(49))
print(h.insert(50))
print(h.insert(51))
print(h.insert(63))
print(h.insert(69))
# print(h.remove(63))
print(h.search(49))
print(h.search(50))
print(h.search(51))
print(h.search(63))
print(h.search(64))
print(h.search(40))
print(h.search(51))
print(h.remove(69))


