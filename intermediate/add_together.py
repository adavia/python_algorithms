def add_together(*args):
    if len(args) > 1:
        if (type(args[0]) is int) and (type(args[1]) is int):
            return args[0] + args[1]
    else:
        if type(args[0]) is int:
            return lambda n: n + args[0] if type(n) is int else None

print(add_together(2, 5))
print(add_together(2)(5))
print(add_together(2)([7]))
print(add_together('http://bit.ly/IqT6zt'))
print(add_together(2, '5'))
