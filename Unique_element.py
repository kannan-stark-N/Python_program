arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

result = []

for num in arr1:
    if num not in arr2:
        result.append(num)

for num in arr2:
    if num not in arr1:
        result.append(num)

print(result)