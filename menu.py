# Menu sys(type options)
    #if no 1 and/or 2 return error
    #if multiple 1 return error
    #if breakfast or dinner and multiple 2 return error
    #if lunch or dinner and multiple 3 return error
    #if dinner and no 4 return error
    #return order

import re

class MenuSystem():
    def __init__(self):
        self.Breakfast = Menu(("Eggs",True,True), ("Toast",True,True), ("Coffee",False,False), (None, True,False))
        self.Lunch = Menu(("Sandwich",True,True), ("Chips",False,True), ("Soda",True,False), (None, True,False))
        self.Dinner = Menu(("Steak",True,True), ("Potatoes",True,True), ("Wine",True,True), ("Cake",True,True))

    def run(self):
        while True:
            print("Enter Order")
            orderInput = input()
            self.getOrder(orderInput)
    
    def getOrder(self, orderInput):
        # check input format (requires alphanumeric characters followed by comma-separated numbers)
        if re.match('^[a-zA-Z]+\s([1-4],)*[1-4]$', orderInput):
            cleanInput = orderInput.lower().split()
            if cleanInput[0] == 'breakfast':
                print(self.Breakfast.setOrder(cleanInput[1].split(',')))
            elif cleanInput[0] == 'lunch':
                print(self.Lunch.setOrder(cleanInput[1].split(',')))
            elif cleanInput[0] == 'dinner':
                print(self.Dinner.setOrder(cleanInput[1].split(',')))
            else:
                print("Unable to Process: invalid menu type")
        else:
            print("Unable to Process: invalid input format")


class Menu():
    def __init__(self, main, side, drink, dessert):
        # set menu
        self.menu = {"main": main[0], "side": side[0], "drink": drink[0], "dessert": dessert[0]}

        # set requirements
        self.menuLimits = {"main": main[1], "side": side[1], "drink": drink[1], "dessert": dessert[1]}
        self.menuReqs = {"main": main[2], "side": side[2], "drink": drink[2], "dessert": dessert[2]}
    
    def setOrderCount(self, input):
        # initialize order counts [main, side, drink, dessert]
        self.itemCounts = [0,0,0,0]

        for i in input:
            i = int(i)
            self.itemCounts[i-1] += 1
        
        # store counts in a dict
        self.menuCounts = {
            "main": self.itemCounts[0], 
            "side": self.itemCounts[1], 
            "drink": self.itemCounts[2], 
            "dessert": self.itemCounts[3]
            }
    
    def setOrder(self, input):
        self.setOrderCount(input)

        status = ""
        order = ""
        success = True

        #check requirements
        for key in self.menu:
            # only check existing menu items
            if key != None:
                # if required item is missing
                if self.menuReqs[key]:
                    if self.menuCounts[key] <= 0 and key != "drink":
                        success = False
                        status = status + f'{key} is missing...'
                    elif key == "drink":
                        order = order + "Water "
                # if multiple of limited item ordered
                if self.menuCounts[key] > 1:
                    if self.menuLimits[key]:
                        success = False
                        status = status + f'{self.menu[key]} cannot be ordered more than once...'
                    else:
                        order = order + f'{self.menu[key]}({self.menuCounts[key]}) '
                elif self.menuCounts[key] == 1:
                    order = order + f'{self.menu[key]} '
            
        # set order result
        if success == False:
            status = "Unable to Process: " + status
            return status
                
        return order

menuSystem = MenuSystem()
menuSystem.run()