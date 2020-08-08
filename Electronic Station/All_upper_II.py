def is_all_upper_II(text: str):
    return True if text.isupper() == True else False


text = "UPPER"
text2 = "lower"
text3 = "is UPPER and lower"
print(is_all_upper_II(text))
print(is_all_upper_II(text2))
print(is_all_upper_II(text3))
