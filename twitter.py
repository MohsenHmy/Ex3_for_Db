from socialMedia import socialMedia 
twitts=[]

class Twitter(socialMedia):
    def __init__(self) :
        super(socialMedia,self).__init__()

    def createNewTwitt(body):
        twit = str(input("Write what you want to twitt: "))
        if(len(twit)< 280):
            twitts.append(twit)
            print("Twit posted succssfully")

        else:
            print("The Twit is too long")


    def getTwitt(self):
        return twitts
