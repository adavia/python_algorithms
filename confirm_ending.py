def confirm_ending(st, target):
    return st[(len(st) - len(target)):] == target
   
print(confirm_ending('Bastian', 'n'))
print(confirm_ending('Congratulation', 'on'))
print(confirm_ending('Connor', 'ne'))
