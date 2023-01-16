
class backpack:
    
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.ajar = False
    def openBag(self):
        if self.ajar == False:
            self.ajar = True
            print("Bag has been opened")
        elif self.ajar == True:
            print("its still opened")
    def closeBag(self):
        if self.ajar == True:
            self.ajar = False
            print("My bag is closed")
        elif self.ajar == False:
            print("Bag is closed very tight")
    def putin(self, item):
        if self.ajar == True:
            self.items.append(item)
            print("item added to bag")
        elif self.ajar == False:
            print("Ah,  the bag is closed")
    def takeout(self, item):
        for ele in self.items:
            if ele == item:
                self.items.remove(item)
                print("My bag is alot lighter")

smallbluebag = backpack("Blue", "Small")
mediumredbag = backpack("Red", "Medium")
largegreenbag = backpack("Green", "Large")

mediumredbag.openBag()
mediumredbag.putin("Lunch")
mediumredbag.putin("Jacket")
mediumredbag.closeBag()
mediumredbag.openBag()
mediumredbag.takeout("Jacket")
mediumredbag.closeBag()