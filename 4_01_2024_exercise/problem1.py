# Develop a program that will enter values of array and display position of element which has value nearest with average of array.
import numpy as np

def find_nearest_pos(arr):
    average = sum(arr)/len(arr)  #calculate average of array
    nearest_value = abs(arr[0]-average)  #initialize nearest value
    nearest_pos = 0
    for i in range(len(arr)):  #using loop to find the nearest value with average
        if abs(arr[i]-average) < nearest_value:
            nearest_value = abs(arr[i]-average)
            nearest_pos = i+1
    return nearest_pos

n = int(input("Enter the number of elements in array: "))
list_ = []
print("Enter the element: ")
for i in range(n):
    e = float(input())
    list_.append(e)
arr = np.array(list_)

print(f"The position of nearest average number is {find_nearest_pos(arr)}")