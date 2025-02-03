"""You are given two numbers n and r. You need to find nCr.
nCr = (n!) / ((n-r)!*(r!))
In recursive way, we can write nCr as nCr = (n-1)C(r-1) + (n-1)Cr

Example 1:

Input:
n = 5, r = 2
Output: 10
Example 2:

Input:
n = 4, r = 1
Output: 4"""

def nCr(n,r):
    if r == 0 or r == n:
        return 1
    return nCr(n-1,r-1) + nCr(n-1,r)
    

