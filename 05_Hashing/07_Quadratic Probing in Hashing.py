def QuadraticProbing(self,hash, hashSize, arr, N):
        #Your code here
        inserted=set()
        for num in arr:
            if num in inserted:
                continue
            inserted.add(num)
            
            index=num%hashSize
            
            if hash[index]==-1:
                hash[index]=num
            else:
                i=1
                while hash[index] !=-1:
                    
                    newIndex = (index+i**2) % hashSize
                
                    if hash[newIndex]==-1:
                        hash[newIndex]=num
                        break
                    i+=1
                    