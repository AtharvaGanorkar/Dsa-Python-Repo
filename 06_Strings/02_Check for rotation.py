s1 = "ABCD"
s2 = "CDAB"

def Rotation_of_Each_Other(s1,s2):
    if len(s1) != len(s2):
        return False
    temp = ""
    temp = s1+s2
    return True if temp.find(s2) else False

print(Rotation_of_Each_Other(s1,s2))