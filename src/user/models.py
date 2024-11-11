class User:
    def __init__(self, username):
        if User.exists(username):
            raise ValueError("Username already exists")
        self.username = username
        self.isOnline = False  # Initialize isOnline to False

    @classmethod
    def exists(cls, username):
        # Assuming there's a method to check if a user exists in the database
        # This is a placeholder for actual database interaction
        return False  # Placeholder return value

    def to_dict(self):
        return {
            "username": self.username,
            "isOnline": self.isOnline  # Include isOnline in the dictionary representation
        }