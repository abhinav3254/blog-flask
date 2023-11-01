class User:
    def __init__(self, name, email, password, role='user', status=True):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.status = status
