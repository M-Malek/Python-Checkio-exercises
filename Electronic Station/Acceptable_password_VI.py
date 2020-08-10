def acceptable_passwordVI(password: str) -> bool:
    is_digit = False
    password = password.lower()

    if len({c for c in password}) < 3: #count len of c (charakter) from password string: take char, count how many of this char contains the string and if it is less than 3, return false
        return False

    if password.find('password') != -1:
        return False
    if len(password) > 9:
        return True if len(password) > 6 else False
    else:
        if password.isdigit() == True:
            return False
        else:
            for i in password:
                if i.isdigit() == True:
                    is_digit = True
        return True if is_digit == True and len(password) > 6 else False


password = "aaaaaa1"
print(acceptable_passwordVI(password))