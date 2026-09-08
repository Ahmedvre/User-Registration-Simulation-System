regiseterd_users = []
faild_registerations = []


def validate_name(name):
    """ validate name lenth to insure it contains at leat 3 charachters"""
    return len(name) >= 3


def validate_email(email):
    """validate if email contain (. and @) """
    return "." in email and "@" in email


def validate_password(password):
    """validate if password meet the requirements: at least (8 characters - 1 upper case - 1 digit)"""
    if len(password) < 8:
        return False
    has_upper = any(p.isupper() for p in password)
    has_diget = any(p.isnumeric() for p in password)
    return has_upper and has_diget


def validate_user_data(name, email, password):
    """validate all user data and raise ValueError if any of the data is invalid"""
    if not validate_name(name):
        raise ValueError('Name must contain at least 3 charachter')

    if not validate_email(email):
        raise ValueError('Email must contain "@" and "."')

    if not validate_password(password):
        raise ValueError('Password must be at least 8 characters long and contain one uppercase letter and one digit.')

    return True


def creeat_user_account(name, email, password):
    """create user account if all data is valid and add it to the registered users list."""

    try:
        validate_user_data(name, email, password)

        if any(user['email'] == email for user in regiseterd_users):
            raise ValueError('Email already registered.')

        user_record = {'name': name, 'email': email, 'password': password, 'status': 'active'}
        regiseterd_users.append(user_record)
        return user_record

    except ValueError as error:
        faild_registerations.append({'name': name, 'email': email, 'password': password, 'error': str(error)})
        return None


creeat_user_account('reda', 'asd@c.com', 'adsA2dsdaad')

print(regiseterd_users)
