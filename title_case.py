def title_case(st):
    splitted = st.split(' ')
    #case_changed = list(map(lambda word: word.capitalize(), splitted))
    case_changed = list(map(lambda word: word[0].upper() + word[1:].lower(), splitted))
    return ' '.join(case_changed)

print(title_case("I'm a little tea pot"))
print(title_case("sHoRt AnD sToUt"))
print(title_case("HERE IS MY HANDLE HERE IS MY SPOUT"))
