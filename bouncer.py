def bouncer(lst):
    return [item for item in lst if bool(item) == True]

print(bouncer([7, "ate", "", False, 9]))
print(bouncer([False, None, 0, [], 1, ""]))
