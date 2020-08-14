def isometric_strings(str1: str, str2: str):
    number_of_elm_str1 = []
    number_of_elm_str2 = []
    for i in range(0, len(str1)):
        number_of_elm_str1.append(str1.count(str1[i]))
        number_of_elm_str2.append(str2.count(str2[i]))

    return True if number_of_elm_str1 == number_of_elm_str2 else False


string1 = "foo"
string2 = "bko"

print(isometric_strings(string1, string2))
