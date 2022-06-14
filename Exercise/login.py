users = [
    {"username": "admin", "password": "admin002"},
    {"username": "ram", "password": "ram002"},
    {"username": "sita", "password": "sita002"},
]
username = input("Username: ")
password = input("Password: ")
increment = 0
login_success = False
while increment < len(users):
    uname = users[increment]["username"]
    upass = users[increment]["password"]
    if username == uname and password == upass:
        login_success = True
        break
    increment += 1
if login_success:
    print(f"Welcome {username}")
else:
    print("Login failed")
