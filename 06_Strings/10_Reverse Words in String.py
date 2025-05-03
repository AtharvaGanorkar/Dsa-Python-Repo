def reverse(s, b, e):
    while b < e:
        s[b], s[e] = s[e], s[b]
        b += 1
        e -= 1

def Reverse_Word(s):
    s = list(s)  # Convert to list for in-place manipulation
    n = len(s)
    b = 0

    # Reverse each word individually
    for e in range(n):
        if s[e] == ' ':
            reverse(s, b, e - 1)
            b = e + 1

    # Reverse the last word
    reverse(s, b, n - 1)

    # Reverse the entire string
    reverse(s, 0, n - 1)

    return ''.join(s)  # Convert back to string

# Input and output
s = input('Enter a string: ')
print("Output:", Reverse_Word(s))
