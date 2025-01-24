l = input("Enter numbers separated by commas: ").split(',')
l = [int(x) for x in l]  # Convert the list elements to integers

sum = 0
for i in l:
    sum += i  # Adding each number to sum

avg = sum / len(l)  # Calculating the average
print(f"The average is: {avg}")


# Way 2



def AVG(l):
    sum = 0
    for x in l:
        sum +=x
    n = len(l)
    avg = sum/n
    return avg

l = [10,50,60,70,40]
print(AVG(l))

#Way 3

def average(l):
    return sum(l)/len(l)

print(average(l))