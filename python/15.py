def validate_login():
    user = input("Enter username: ").strip()
    pwd = input("Enter password: ").strip()
    if not user or not pwd:
        print("Username and password cannot be blank")
        return
    
    if user == "sankar":
        if pwd == "pass123":
            print("Login successful")
        else:
            print("Invalid password")
    else:
        print("Invalid username")

validate_login()
