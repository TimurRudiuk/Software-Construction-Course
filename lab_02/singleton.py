class Authenticator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Authenticator, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self.users = {}
        self.logged_in_users = set()

    def add_user(self, username, password):
        self.users[username] = password

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            self.logged_in_users.add(username)
            return True
        return False

    def logout(self, username):
        if username in self.logged_in_users:
            self.logged_in_users.remove(username)

    def is_logged_in(self, username):
        return username in self.logged_in_users

def task3_demo():
    auth1 = Authenticator()
    auth1.add_user("admin", "admin123")
    auth1.add_user("user1", "password1")

    auth2 = Authenticator()
    print(f"Same instance? {auth1 is auth2}")

    print("Logging in 'admin' with wrong password:", auth2.login("admin", "wrong"))
    print("Logging in 'admin' with correct password:", auth1.login("admin", "admin123"))

    print("Is 'admin' logged in?", auth2.is_logged_in("admin"))

    auth1.logout("admin")
    print("After logout, is 'admin' logged in?", auth2.is_logged_in("admin"))

if __name__ == "__main__":
    print("\n=== Task 3: Singleton ===")
    task3_demo()