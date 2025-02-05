def CountOccurance(arr,x):
    count = 0
    for i in range(len(arr)):
        if arr[i] == x:
            count +=1
    return count
    

# arr = [10,20,20,20,30,30]
arr = [10,10,10,10]
x = 10

print(CountOccurance(arr,x))

def CoutOcc(l,x):
    first = FirstOccurance(l,x)   # FirstOccurance() and LastOccurance()
                                  # is the function already derived , here we use that
    if first == -1:
         return 0
    else:
        return LastOccurance(l,x) - first + 1  # this is the formula [lastoccurance - first + 1]
