class User:
    all_posts = {}
    user_id = 0
    def __init__(self, name, email, d_license):
        self.name = name
        self.email = email
        self.d_license = d_license
        self.posts = []
        self.id = User.user_id + 1
        User.user_id += 1
    
    def create_post(self, msg):
        self.posts.append(msg)
        if User.all_posts.get(self.name):
            User.all_posts[self.name] += [msg]
        else:
            User.all_posts[self.name] = [msg]
    
    def delete_post(self, msg):
        self.posts.remove(msg)
        User.all_posts[self.name].remove(msg)
        