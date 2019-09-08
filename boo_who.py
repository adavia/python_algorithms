def boo_who(expr):
    return isinstance(expr, bool)

print(boo_who([1,2,4]))
print(boo_who(False))
print(boo_who(True))
print(boo_who(1))
print(boo_who('True'))
print(boo_who([]))
