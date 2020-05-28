#8min
n = int(input())
arr = [int(i) for i in input().split(' ')]
sum = 0
even = 0
odd = 0
for num in arr:
    sum += num
    if num % 2 == 0:
        even += 1 
    else:
        odd += 1
if sum % 2 == 0:
    print(even)
else:
    print(odd)


        