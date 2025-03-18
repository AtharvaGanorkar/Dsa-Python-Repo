s1 = input("Enter a First String : ")
s2 = input("Enter a Second String : ")

def IsSubsequence(s1,s2):
    i = 0
    j = 0
    while i<len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i +=1
            j +=1
        else:
            i +=1
    if j == len(s2):
        return True
    else:
        return False
        
print(IsSubsequence(s1,s2)) 

def IsSubsequence(s1,s2,m,n):
    if n == 0:
         return True
    
    if m == 0:
        return False
    if s1[n-1] == s2[m-1]:
        return IsSubsequence(s1,s2,m-1,n-1)
    else:
        return IsSubsequence(s1,s2,m-1,n)
    
