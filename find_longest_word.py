def find_longest_word(sentence):
    # Easier solution
    # return max([len(word) for word in splitted])

    splitted = sentence.split(' ')
    longest = 0

    for word in splitted:
        if len(word) > longest:
            longest = len(word)

    return longest

print(find_longest_word("May the force be with you"))
print(find_longest_word("What is the average airspeed velocity of an unladen swallow"))
print(find_longest_word("What if we try a super-long word such as otorhinolaryngology"))
