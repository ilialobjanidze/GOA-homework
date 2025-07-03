def alphanumeric(password):
    # Check that the password is not empty and contains only alphanumeric characters (letters and digits)
    return len(password) > 0 and password.isalnum()
