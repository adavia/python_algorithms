def vowels(st):
    vowels = 'aeiou'
    counter = 0

    for char in st.lower():
        if char in vowels:
            counter += 1

    return counter

print(vowels('Hi there!'))
print(vowels('Why do you ask?'))
print(vowels('Why?'))
