""""
Develop a program that will enter the values of the array and display the different numbers in the above array.
The output from your program looks something like:  
input: 6 8 5 4 6 8 9 1 4 9 12
output: 6 8 5 4 9 1 12
"""

def unique_value(arr):
    unique_arr = []
    for i in range(len(arr)):
        if arr[i] not in unique_arr:
            unique_arr.append(arr[i])
    return " ".join(unique_arr)

input_arr = input("Enter the values of the array separated by space: ")
arr = input_arr.split()

print(unique_value(arr))