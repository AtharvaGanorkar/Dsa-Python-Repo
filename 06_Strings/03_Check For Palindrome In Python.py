S = input("Enter a string: ")
def IsPalandrome(S):
    low = 0
    high = len(S)-1

    while low < high:
        if S[low] != S[high]:
            print("NO")
            break
        low +=1
        high -=1
        
    else:
        print("YES")

IsPalandrome(S)

S = input("Enter a string: ")
def IsPalandrome(S):
    if S == S[::-1]:
        print("YES")
    else:
        print("NO")


IsPalandrome(S)