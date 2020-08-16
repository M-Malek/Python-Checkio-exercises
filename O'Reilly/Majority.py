def is_majority(items: list):
    return True if items.count(True) > items.count(False) else False


logical_list = [True, True, False, True]
print(is_majority(logical_list))
