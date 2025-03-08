def Seprate_Chaining(arr,sizeOfArray):
    hashSize = len(arr)-1
    table = [[] for i in range(hashSize)]

    for i in range(sizeOfArray):
        index = arr[i]%hashSize
        table[index].append(arr[i])
        print(table)

arr = [92,4,14,24,44,91]
Seprate_Chaining(arr,6)