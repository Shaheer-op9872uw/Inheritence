class Bird:

    def __init__(slef):
        print("bird is ready")

    def whoisThis (self):
        print("Bird")

    def swim(self):
        print("swim faster faster")

class Penguin(Bird):
    
    def __init__(self):

        super().__init__()
        print("Penguin is deady")

    def whoisThis(self):
        print("i am a penguin")
        

    def run(self):
        print("TURBO BOOSTER MODE ON!")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()