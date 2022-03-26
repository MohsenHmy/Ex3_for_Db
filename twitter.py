from socialMedia import socialMedia 

class Twitter(socialMedia):
    def __init__(self) :
        super().__init__("twitter")
        self.twitts=[]

    def createNewTwitt(self, body):
        if(len(body)< 280):
            self.twitts.append(body)
            print("Twit posted succssfully")

        else:
            print("The Twit is too long")


    def getTwitt(self):
        return self.twitts
