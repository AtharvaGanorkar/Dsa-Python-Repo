String =  input("Enter a string: ")
def Reverse(String):
    rev = ""
    for i in String:
        rev = i + rev
    print(rev)
        
    
Reverse(String)


String =  input("Enter a string: ")
def Reverse(String):
    print(String[::-1])

Reverse(String)