def flatten(dictionary, parent_key='', separator='/'):
    flat = []
    for key, value in dictionary.items():
        new_key = parent_key + separator + key if parent_key else key
        if value == {}:
            value = ""
        if type(value) == dict:
            flat.extend(flatten(value, new_key, separator=separator).items())
        else:
            flat.append((new_key, value))

    return dict(flat)


dic_1 = {"key": "value"}
dic_2 = {"key": {"deeper": {"more": {"enough": "value"}}}}
dic_3 = {"empty": {}}
dic_4 = {"name": {
    "first": "One",
    "last": "Drone"},
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}}}
print(flatten(dic_3))
