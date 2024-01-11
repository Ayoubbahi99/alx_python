def validate_password(password):
    if len(password) < 8:
        return False
    
    for char in password:
        if not char.islower():
            return False
        
    for char in password:
        if not char.isupper():
            return False

    for char in password:
        if not char.isdigit():
            return False
    if " " in password:
        return False
    return True