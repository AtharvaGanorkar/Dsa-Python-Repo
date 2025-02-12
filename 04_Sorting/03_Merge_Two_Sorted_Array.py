a = [10,15]
b = [5,6,6,30,40]
res = []

def MergeTwoArrayInSortedManner(a,b):
            res = []
            m = len(a)
            n = len(b)
            i = 0
            j = 0
            while i < m and j < n:
                if a[i] > b[j]:
                    res.append(b[j])
                    j = j+1
                else:
                    res.append(a[i])
                    i = i+1
            while i < m:
                  res.append(a[i])
                  i +=1
            while j < n:
                  res.append(b[j])
                  j +=1
            return res

print(MergeTwoArrayInSortedManner(a,b))