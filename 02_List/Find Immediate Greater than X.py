def immediateGreater(self,arr,n,x):
        result = -1
        for num in arr:
            if num > x:
                if result == -1 or num < result:
                    result = num
        return result


n = 5
arr= [63,6,60,38,3,94,43,83,65]
x = 18

def immediateGreater(arr,n,x):
        res=[]
        for y in arr:
            if y>x:
                res.append(y)
                res.sort()
        return res[0]

print(immediateGreater(arr,n,x))


