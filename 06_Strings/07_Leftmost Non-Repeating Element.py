def leftMostNonRepeating(str):
    for i in range(len(str)):
        flag =False
        for j in range(i+1,len(str)):
            if str[i] == str[j]:
                flag = True
                break

        if flag == False:
            return i
        
    return -1
str = "geeksforgeeks"
print(leftMostNonRepeating(str))

def leftMostNonRepeating(str):
    count = [0]*256

    for i in range(len(str)):
        if str[i] in str:
            count[ord(str[i])] +=1
    
    for i in range(len(str)):
        if count[ord(str[i])] == 1:
            return i
    return -1


str = "geeksforgeeks"
print(leftMostNonRepeating(str))