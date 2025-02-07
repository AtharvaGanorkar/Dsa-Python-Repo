def squareRoot(x):
    res = 1
    while res * res <= x:
        res +=1
    return res-1

print(squareRoot(15))


def squareRoot(x):
    low = 1
    high = x
    ans = -1
    while low <= high:
        mid = low + (high - low)//2
        Msq = mid * mid
        if Msq == x:
            return mid
        elif Msq > x:
            high = mid - 1
        else:
            low = mid + 1
            ans = mid
    return ans