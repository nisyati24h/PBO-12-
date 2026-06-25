class User:

    def __init__(self, username, screen_limit):
        self.__username = username
        self.__screen_limit = screen_limit

    def get_username(self):
        return self.__username

    def get_screen_limit(self):
        return self.__screen_limit

    def set_screen_limit(self, limit):
        self.__screen_limit = limit