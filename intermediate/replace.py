def replace(st, before, after):
    # Easiest way 
    # return st.replace(before, after)

    # Another way
    # index = st.index(before)
    # after = after.capitalize() if before[0].isupper() else after
    # return st[:index] + after + st[index + len(before):]

    lst = st.split(' ')
    
    for i in range(len(lst)):
        if lst[i] == before:
            if before[0].isupper():
                lst[i] = after.capitalize()
            else:
                lst[i] = after

    return ' '.join(lst)

print(replace('A quick brown fox jumped over the lazy dog', 'jumped', 'leaped'))
print(replace('Let us get back to more Coding', 'Coding', 'algorithms'))
print(replace('This has a spellngi error', 'spellngi', 'spelling'))
print(replace('His name is Tom', 'Tom', 'john'))
