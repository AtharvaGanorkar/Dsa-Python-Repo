"""GCD Euclid

You are given two numbers a and b. Find their GCD using recursion.

Example 1:

Input:
a = 7, b = 8
Output: 1
Example 2:

Input:
a = 2, b = 4
Output: 2"""

 def GCD(self,a,b):
        if a > b:
            n = a
        else:
            n = b
        def D(n):
            if n == 1:
                return 1
            if a%n == 0 and b%n == 0:
                return n
            return D(n-1)
        
        return D(n)