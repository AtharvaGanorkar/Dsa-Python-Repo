#User function Template for python3

"""
input - 
s = string given 

output - 
return 0 if not validated else return true
"""

"""Given a string s representing a password, you need to check if the string is valid or not. A valid string has the following properties:

String must have the length greater than or equal to 10.
String must contain at least 1 numeric character.
String must contain at least 1 uppercase character.
String must contain at least 1 lowercase character.
String must contain at least 1 special character from @#$-*.
 

Example 1:

Input: eHello123@
Output: 1
Explanation: String is valid."""


def validate(s):
    #your code here
    char=[0]*5
    if len(s)>=10:
        char[0]=1
    for i in range(len(s)):
        if s[i] in ("1","2","3","4","5","6","7","8","9","0"):
            char[1]=1
        elif ord(s[i])>=65 and ord(s[i])<=90:
            char[2]=1
        elif ord(s[i])>=97 and ord(s[i])<=122:
            char[3]=1 
        else:
            char[4]=1
    for i in char:
        if i==0:
            return 0
    return 1        
             