"""You are given a number n. You need to see if the number is a palindrome or not (recursively)

Example 1:

Input:
n = 100
Output: 0
Example 2:

Input:
n = 101
Output: 1"""


def isPalin(N):
        def check_palindrome(n,num_digits):
            if n == 0 and num_digits <= 1:
                return True
            
            First_digit = n // (10**(num_digits - 1))
            Last_digit = n%10
            
            if First_digit != Last_digit:
                return False
                
            return check_palindrome(n % (10 ** (num_digits - 1)) // 10 , num_digits -2)
            
        num_digits = len(str(N))
        
        if check_palindrome(N,num_digits):
            return 1
        else:
            return 0

print(isPalin(100))

def isPalandrome(str,start,end):
    if start>=end:
        return True
    return (str[start] == str[end] and isPalandrome(str,start+1,end-1))


# A recursive Python program
# to check whether a given
# number is palindrome or not

def isPalRec(st, s, e) :
	
	if (s == e):
		return True

	if (st[s] != st[e]) :
		return False

	if (s < e + 1) :
		return isPalRec(st, s + 1, e - 1);

	return True

def isPalindrome(st) :
	n = len(st)
	
	if (n == 0) :
		return True
	
	return isPalRec(st, 0, n - 1);


st = "geeg"
if (isPalindrome(st)) :
	print("Yes")
else :
	print("No")