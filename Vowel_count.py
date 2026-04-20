def count_vowels(arr):
    count = 0
    vowels = "aeiouAEIOU"
    
    for char in arr:
        if char in vowels:
            count += 1
            
    return count

arr = "Hello World"
print(count_vowels(arr))
