def acceptable_password_I(password: str):
    return True if len(password) > 6 else False


def acceptable_password_II(password: str):
    for i in password:
        if i.isdigit() == True:
            return True if len(password) > 6 else False
        else:
            pass
    #return True if len(password) > 6 else False


def acceptable_password_II(password: str):
    is_digit = False
    for i in password:
        if i.isdigit() == True:
            is_digit = True
    return True if is_digit == True and len(password) > 6 else False


def acceptable_password_III(password: str) -> bool:
    is_digit = False
    if password.isdigit() == True:
        return False
    else:
        for i in password:
            if i.isdigit() == True:
                is_digit = True
    return True if is_digit == True and len(password) > 6 else False


def acceptable_password_IV(password: str) -> bool:
    is_digit = False
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


password = "muchlonger5"
print(acceptable_password_I(password))
print(acceptable_password_II(password))
print(acceptable_password_III(password))
print(acceptable_password_IV(password))
