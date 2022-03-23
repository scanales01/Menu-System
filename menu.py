# Menu sys(type options)
    #if no 1 and/or 2 return error
    #if multiple 1 return error
    #if breakfast or dinner and multiple 2 return error
    #if lunch or dinner and multiple 3 return error
    #if dinner and no 4 return error
    #return order 

class MenuSystem():
    def __init__(self):
        self.breakfast = Menu(["Eggs",True], ["Toast",True], ["Coffee",False], [None, True])

    def run(self):
        while True:
            print("Enter Order")
            orderInput = input()
            self.getOrder(orderInput)
    
    def getOrder(self, orderInput):
        cleanInput = orderInput.lower().split()
        if cleanInput[0] == 'breakfast':
            print(self.breakfast.setOrder(cleanInput[1].split(',')))

class Menu():
    def __init__(self, main, side, drink, dessert):
        # set menu
        self.main = main[0]
        self.side = side[0]
        self.drink = drink[0]
        self.dessert = dessert[0]
        self.menu = [self.main, self.side, self.drink, self.dessert]
        self.menu = [x for x in self.menu if x != None]

        # set max
        self.mainMax = main[1]
        self.sideMax = side[1]
        self.drinkMax = drink[1]
        self.dessertMax = dessert[1]
    
    def setOrderCount(self, input):
        # initialize order counts
        self.mainCount = 0
        self.sideCount = 0
        self.drinkCount = 0
        self.dessertCount = 0

        for i in input:
            i = int(i)
            if i == 1:
                self.mainCount += 1
            elif i == 2:
                self.sideCount += 1
            elif i == 3:
                self.drinkCount += 1
            elif i == 4:
                self.dessertCount += 1
    
    def setOrder(self, input):
        self.setOrderCount(input)

        order = ""
        success = True

        # check for requirements
        if self.mainCount <= 0:
            success = False
            order = order + "Main is missing..."
        elif self.mainMax and self.mainCount > 1:
            success = False
            order = order + f'{self.main} cannot be ordered more than once...'

        if self.sideCount <= 0:
            success = False
            order = order + "Side is missing..."
        elif self.sideMax and self.sideCount > 1:
            success = False
            order = order + f'{self.side} cannot be ordered more than once...'

        if  self.drinkCount > 1 and self.drinkMax:
            success = False
            order = order + f'{self.drink} cannot be ordered more than once..'

        if self.dessert == None and self.dessertCount > 0:
            success = False
            order = order + "Dessert unavailable..."
        elif self.dessert != None and self.dessertCount <= 0:
            success = False
            order = order + "Dessert is missing..."
        elif self.dessertMax and self.dessertCount > 1:
            success = False
            order = order + f'{self.dessert} cannot be ordered more than once...' 


        if success == False:
            order = "Unable to Process: " + order
        else:
            #set order
            if self.drinkCount <= 0:
                order = f'{self.main}, {self.side}, Water'
            else:
                order = " ".join(self.menu)
        
        return order
        


menuSystem = MenuSystem()
menuSystem.run()