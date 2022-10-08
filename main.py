
numbers = list(map(int, input().split()))
average = 0

for i in range(len(numbers)):
    average += numbers[i]
average = average / len(numbers)

for j in range(len(numbers)):
    numbers[j] = abs(average - numbers[j])
    print (f'{numbers[j]:.2f}', end=' ')

# Use this statement to print out the list element. # Replace the variable 'dist' with your variable
# print (f'{dist:.2f}', end=' ')