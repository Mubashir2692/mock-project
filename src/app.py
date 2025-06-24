# src/app.py
def main():
    print("Welcome to the Mock Project!")

def login(username, password):
    if username == "admin" and password == "secret":
        return "Login successful!"
    return "Login failed!"

if __name__ == "__main__":
    main()