#find frequence duplicate
def duplicates(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    duplicates = {}
    for key, value in freq.items():
        if value > 1:
            duplicates[key] = value
    return duplicates
arr = [int (x) for x in input().split()]
print(duplicates(arr))


#missind number
arr = [3,2,4,1,5,7,9,6,10]
total=0
for i in arr:
    total+=i
l=len(arr)+1
n=(l*(l+1))/2
print(int(n-total))


#rotate the order
arr=[1,2,3,5,4]
arr.sort()
print(arr)


#find maximum order
def max_order(arr):
    arr.sort()
    order1 = arr[-1] * arr[-2]
    order2 = arr[0] * arr[1]
    return max(order1, order2)
print(max_order([1, 2, 3, 4]))
print(max_order([0, -2, 2, 1]))


#checking if two array are equal
def equal(arr1, arr2):
    return sorted(arr1) == sorted(arr2)
arr1=[int(x)for x in input().split()]
arr2=[int(y)for y in input().split()]
print(equal(arr1,arr2))


#plus one number
arr=[1,2,3]
a=0
for i in arr:
    a=a*10+i
a+=1
s=str(a)
lst=[]
for i in s:
    lst.append(i)
print(lst)


#move all zeros to the end
def move_zeros(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
    for i in range(j, len(arr)):
        arr[i] = 0
    return arr
print(move_zeros([0, 1, 0, 3, 12]))


#find the second largest element
arr = [1,2,3,4,5,8,100,1,3]
first=arr[0]
second=arr[0]
for i in arr:
    if i>first:
        second=first
        first=i
    elif i>second:
        second=i
print(second)