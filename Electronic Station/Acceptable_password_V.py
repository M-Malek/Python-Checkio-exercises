def acceptable_passwordV(password: str) -> bool:
    is_digit = False
    password = password.lower()
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


password = "password12345"
print(acceptable_passwordV(password))
