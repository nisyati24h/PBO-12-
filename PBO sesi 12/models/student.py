from models.user import User

class Student(User):
    def __init__(self, username, screen_limit, major):
        super().__init__(username, screen_limit)
        self.major = major