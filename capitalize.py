def capitalize(st):
    split_st = st.split(' ')
    return ' '.join([word[0].upper() + word[1:] for word in split_st])

print(capitalize('a short sentence'))
print(capitalize('a lazy fox'))
print(capitalize('look, it is working!'))
