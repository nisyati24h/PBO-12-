from models.user import User

class Worker(User):
    def __init__(self, username, screen_limit, company):
        super().__init__(username, screen_limit)
        self.company = company