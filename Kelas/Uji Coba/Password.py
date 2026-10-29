password = input("Enter Password: ")
has_upper, has_number, has_special = False, False, False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.isdigit():
        has_number = True
    elif not char.isalnum():
        has_special = True
if len(password) >= 8 and has_upper and has_number and has_special:
    print("Strong Password")
else:
    print("Weak Password")