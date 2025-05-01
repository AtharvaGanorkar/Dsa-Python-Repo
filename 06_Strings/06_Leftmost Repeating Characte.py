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

# Leftmost Repeating Character
# Efficient 2

CHAR = 256
def leftmost(st) :
    vis = [False] * CHAR
    res = -1
    for i in range(len(st)-1,-1,-1) :
        if (vis[ord(st[i])]==True) :
            res = i
        else :
            vis[ord(st[i])] = True
    
    return res
        
st = "abccbd"
print(leftmost(st))
