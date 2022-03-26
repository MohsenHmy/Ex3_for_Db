from socialMedia import socialMedia


posts = []
class instagram(socialMedia):
    def __init__(self):
        super(socialMedia,self).__init__()
        self.posts=[]

    def publishNewPost(body):
        pst = str(input("Write what you want to post: "))
        if(len(pst)< 2200):
            posts.append(pst)
            print("Post posted succssfully")

        else:
            print("The post is too long")

    def getPost(self):
        return posts