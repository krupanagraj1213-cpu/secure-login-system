

```python id="gmwtth"
import hashlib

# Simple user database
users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed = hash_password(password)
    users[username] = hashed

    print("User registered successfully!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed = hash_password(password)

    if username in users and users[username] == hashed:
        print("Login successful!")
    else:
        print("Invalid username or password")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
