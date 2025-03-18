def leftmost(str):
    for i in range(len(str)):
        for j in range(i+1, len(str)):
            if str[i] ==  str[j]:
                return i
    return -1

def leftmost(str):
    count = [0]*256
    for i in range(len(str)):
        count[ord(str[i])] +=1
    for i in range(len(str)):
        if count[ord(str[i])] > 1:
            return i
    return -1

def leftmost(st):
    char_map = {}
    res = -1
    for i in range(len(st)-1, -1, -1):
        if st[i] in char_map:
            res = i
        else:
            char_map[st[i]] = True
    return res

print(leftmost("abccbd"))  # Output: 1
