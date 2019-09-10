def check_name(collection, source):
    keys = source.keys()
    
    def filter_keys(item):
        for key in keys:
            if key not in item or item[key] != source[key]:
                return False
        return True

    return list(filter(filter_keys, collection))

    # return result
    # for item in collection:
    #     if all(key in item for key in keys):
    #         for key in keys:
    #             if item[key] == source[key]:
    #                 result.append(item)

print(check_name([{"first": "Romeo", "last": "Montague" }, {"first": "Mercutio", "last": None }, {"first": "Tybalt", "last": "Capulet" }], {"last": "Capulet" }))
print(check_name([{"apple": 1 }, { "apple": 1}, {"apple": 1, "bat": 2}], {"apple": 1}))
print(check_name([{"apple": 1, "bat": 2}, {"bat": 2 }, {"apple": 1, "bat": 2, "cookie": 2}], {"apple": 1, "bat": 2}))
