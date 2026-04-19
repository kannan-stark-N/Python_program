arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

result = []

for num in arr1:
    if num in arr2 and num not in result:
        result.append(num)

print(result)