arr = [1, 2, 3, 4, 5]
k = 2

for i in range(k):
    first = arr.pop(0)
    arr.append(first)

print(arr)