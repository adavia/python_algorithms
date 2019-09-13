def truthy_checker(collection, pre):
    return all([pre in item and bool(item[pre]) for item in collection])

print(truthy_checker([{"user": "Tinky-Winky", "sex": "male"}, {"user": "Dipsy", "sex": "male"}, {"user": "Laa-Laa", "sex": "female"}, {"user": "Po", "sex": "female"}], "sex"))
print(truthy_checker([{"user": "Tinky-Winky", "sex": "male"}, {"user": "Dipsy"}, {"user": "Laa-Laa", "sex": "female"}, {"user": "Po", "sex": "female"}], "sex"))
print(truthy_checker([{"user": "Tinky-Winky", "sex": "male", "age": 0}, {"user": "Dipsy", "sex": "male", "age": 3}, {"user": "Laa-Laa", "sex": "female", "age": 5}, {"user": "Po", "sex": "female", "age": 4}], "age"))
print(truthy_checker([{"name": "Pete", "onBoat": True}, {"name": "Repeat", "onBoat": True, "alias": "Repete"}, {"name": "FastFoward", "onBoat": True}], "onBoat"))
print(truthy_checker([{"single": "double"}, {"single": None}], "single"))
