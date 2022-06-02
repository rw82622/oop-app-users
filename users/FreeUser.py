from users.User import User

class FreeUser(User):
    
    def create_post(self, msg):
        if len(self.posts) < 2:
            super().create_post(msg)