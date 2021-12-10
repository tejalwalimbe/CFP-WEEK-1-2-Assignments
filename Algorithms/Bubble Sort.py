arr = []
number = int(input("Please Enter Number of Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Element of List1 : " %i))
    arr.append(value)

for i in range(number -1):
    for j in range(number - i - 1):
        if(arr[j] > arr[j + 1]):
             temp = arr[j]
             arr[j] = arr[j + 1]
             arr[j + 1] = temp

print("Sorted Elements are : ", arr)