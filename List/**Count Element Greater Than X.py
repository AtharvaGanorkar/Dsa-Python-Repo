def greaterThanX(arr,n,x):
        res = []
        for y in arr:
            if y>x:
                res.append(y)
                
        return len(res)