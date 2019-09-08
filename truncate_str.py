def truncate_str(st, num):
    if len(st) > num:
        return st[:num] + '...'
    
    return st

print(truncate_str('A-tisket a-tasket A green and yellow basket', 8))
print(truncate_str('Peter Piper picked a peck of pickled peppers', 11))
print(truncate_str('A-tisket a-tasket A green and yellow basket', len('A-tisket a-tasket A green and yellow basket')))
