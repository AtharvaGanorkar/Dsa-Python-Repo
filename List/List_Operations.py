l = [10,20,30,40,50,60]

l.append(30)
print(l)

l.insert(1,15)
print(l)

print(15 in l)

print(l.count(30))

print(l.index(30))

print(l.index(30,4,8))

l.remove(20)
print(l)

print(l.pop())
print(l)

print(l.pop(2))
print(l)

del l[1]
print(l)

del l[0:2]
print(l)

l2 = [10,40,20,50]
print(max(l2))

print(min(l2))

print(sum(l2))

l2.reverse()
print(l2)

l2.sort()
print(l2)
