from socialMedia import socialMedia

class instagram(socialMedia):
    def __init__(self):
        super().__init__("instagram")
        self.posts=[]

    def publishNewPost(self, body):
        if(len(body)< 2200):
            self.posts.append(body)
            print("Post posted succssfully")

        else:
            print("The post is too long")

    def getPost(self):
        return self.posts
