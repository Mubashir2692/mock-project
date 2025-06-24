# src/app.py
def main():
    print("Welcome to the Mock Project!")

def login(username, password):
    if username == "admin" and password == "password123":
        return "Authenticated successfully!"
    return "Authentication failed!"

if __name__ == "__main__":
    main()