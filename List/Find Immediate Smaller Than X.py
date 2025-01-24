N = 5
arr = [4,67,13,12,15] 
X = 16

def immediateSmaller(arr,N,X):
        res=[]
        if X == 1:
            return -1
        for y in arr:
            if y<X:
                res.append(y)
                res.sort()
        return res[-1]
print(immediateSmaller(arr,N,X))


def immediateSmaller(arr,N,X):
        closest_smaller = -1
        for num in arr:
            if num<X:
                if closest_smaller == -1 or X - num<X - closest_smaller:
                    closest_smaller = num
        return closest_smaller

print(immediateSmaller(arr,N,X))