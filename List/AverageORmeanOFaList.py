l = input("Enter numbers separated by commas: ").split(',')
l = [int(x) for x in l]  # Convert the list elements to integers

sum = 0
for i in l:
    sum += i  # Adding each number to sum

avg = sum / len(l)  # Calculating the average
print(f"The average is: {avg}")