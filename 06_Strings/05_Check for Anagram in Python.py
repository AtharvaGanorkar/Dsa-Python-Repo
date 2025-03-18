s1 = input("Enter a First String : ")
s2 = input("Enter a Second String : ")

'''def CheckAnagram(s1,s2):
    i = 0
    if len(s1) != len(s2):
        return 'NO'
    while i < len(s1):
        if s1[i] not in s2:
            break
        elif s2[i] not in s1:
            break
        else:
            i +=1
    if i != len(s1):
        return 'No'
    return 'Yes'
    
print(CheckAnagram(s1,s2))

s1 = input("Enter a First String : ")
s2 = input("Enter a Second String : ")

def CheckAnagram(s1,s2):
    if len(s1) != len(s2):
        return 'NO'
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        return "Yes"
    else:
        return "NO"
        
print(CheckAnagram(s1,s2))'''

def CheckAnagram(s1,s2):
    if len(s1) != len(s2):
        return 'NO'
    
    count = [0]*256
    for i in range(len(s1)):
        count[ord(s1[i])] +=1
        count[ord(s1[i])] +=1

    for x in count:
        if x!= 0:
            return "No"
    return "Yes"

print(CheckAnagram(s1,s2))       