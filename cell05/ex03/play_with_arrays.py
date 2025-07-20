#!/usr/bin/env python3
original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
for num in original_array:
    if num > 5:
        new_array.append(num + 2)
unique_array = []
for num in new_array:
    if num not in unique_array:
        unique_array.append(num)
print(original_array)
print(unique_array)