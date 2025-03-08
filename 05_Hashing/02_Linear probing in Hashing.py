def LinearProbing(arr,hashSize,sizeOfArray):
    table = [-1 for i in range(hashSize)]

    for i in range(sizeOfArray):
        index = arr[i] % hashSize
        if table[index] == -1:
            table[index] = arr[i]

        else:
            k = arr[i] % hashSize
            flag= 0
            counter = 0
            while counter < hashSize and table[k] != -1:
                if table[k] == arr[i]:
                    flag = 1
                    break
                k = (k + 1)%hashSize
                counter +=1

            if flag == 1:
                continue
            if counter < hashSize:
                table[k] = arr[i]   
    
    return table

