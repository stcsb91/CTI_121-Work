class User:

    def __init__(self, first_name, last_name, username, email,):
        """Initialize/create the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email_address = email
        self.login_attempts = 0

    def describe_user(self):
        """Display user information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email_address}")
        

#This part is basically the same as the Chapter method example, I hope
    def increase_login_attempts(self):
        """Increase the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0

#Using my dog, Lola here since there are no security or personal info issues
lola = User('lola', 'starr-baum', 'GreatDane21', 'squirellchaser@gmail.com',)
lola.describe_user()

print("Making 3 login attempts...")
lola.increase_login_attempts()
lola.increase_login_attempts()
lola.increase_login_attempts()
print(f"Login attempts: {lola.login_attempts}")

print("Resetting login attempts...")
lola.reset_login_attempts()
print(f"Login attempts: {lola.login_attempts}")