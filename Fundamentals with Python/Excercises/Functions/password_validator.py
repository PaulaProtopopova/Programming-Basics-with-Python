# --------------------------------CONDITION OF THE TASK-------------------------------
# Write a function that checks if a given password is valid. Password validations are:
# • It should be 6 - 10 (inclusive) characters long
# • It should consist only of letters and digits
# • It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# • "Password must be between 6 and 10 characters"
# • "Password must consist only of letters and digits"
# • "Password must have at least 2 digits"

# --------------------------OPTION 1 ONE FUNCTION---------------------------


# def pass_validation(password):
#     password_is_valid = True
#     if len(password) not in range(6,11):
#         password_is_valid = False
#         print("Password must be between 6 and 10 characters")
#     if not password.isalnum():
#         password_is_valid = False
#         print("Password must consist only of letters and digits")
#     counter_of_digits = 0
#     for character in password:
#         if character.isdigit():
#             counter_of_digits += 1
#     if counter_of_digits < 2:
#         password_is_valid = False
#         print('Password must have at least 2 digits')
#     return password_is_valid
#
#
# some_password = input()
# password_is_valid = pass_validation(some_password)
# if password_is_valid:
#     print('Password is valid')


# --------------------------------OPTION 2 - THREE FUNCTIONS--------------------

def lenght(some_password):
    if len(password) not in range(6, 11):
        print("Password must be between 6 and 10 characters")
        return False
    return True


def symbols(some_password):
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        return False
    return True

def two_digits(some_password):
    digit_counter = 0
    for char in password:
        if char.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        return False
    return True


password = input()

validations = [lenght(password), symbols(password), two_digits(password)]

if all(validations):
    print("Password is valid")


