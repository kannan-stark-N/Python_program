def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    
    for char in s:
        if char in vowels:
            count += 1
            
    return count

text = "Hello World"
print(count_vowels(text))