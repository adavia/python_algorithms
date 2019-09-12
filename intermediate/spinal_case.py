# import re

# def spinal_case(s):
#     match = re.split(r'(?=[A-Z])|_|-|\s', s.lower())
#     return '-'.join(filter(lambda x: x != '', match))
    
# print(spinal_case('This-Is-Spinal-Tap'))
# print(spinal_case('This_Is_Spinal_Tap'))
# print(spinal_case('This Is Spinal Tap'))
# print(spinal_case('ThisIsSpinalTap'))
# print(spinal_case('Teletubbies say Eh-oh'))
# print(spinal_case('AllThe-small Things'))

def test_kwargs(fe, arg):
    print(arg, fe)


test_kwargs(arg='nooooo', bi=45)
