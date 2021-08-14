class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

r1 = Rider("Yukka")
h1 = Horse("Whity", r1)
print(h1.rider.name)
