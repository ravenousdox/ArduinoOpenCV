from PIL import Image
import pyautogui
import time
import pickle

validActions = {
    'SHRINK'    : 16,
    'UPSET'     : 13,
    'BEND'      : 7,
    'PUNCH'     : 2,
    'HIT_LIGHT' : -3,
    'HIT_MEDIUM': -6,
    'HIT_HARD'  : -9,
    'DRAW'      : -15 
}

actionsToCoordinates = {
    'SHRINK'    : [1013,491],
    'UPSET'     : [977,491],
    'BEND'      : [1013,455],
    'PUNCH'     : [977,455],
    'HIT_LIGHT' : [907,455],
    'HIT_MEDIUM': [946,455],
    'HIT_HARD'  : [907,491],
    'DRAW'      : [946,491]
}

menu = {
    'LIST'       : listOptions(),
    'SMITH'      : performSmith(),
    'MODIFY'     : modifySmithingItem(),
    'CREATE'     : createSmithingItem(),
    'REGENERATE' : regenerateFile(),
    'RELOAD'     : reloadFile(),
    'INITIALIZE' : initializeItems(),
    'EXIT'       : terminateProgram()
}

#List of initialization values for each vanilla SmithingItem
#Uses the template: Name, RuleSet, Offset
vanillaItems = [
    ['Sheet', ['HIT_LIGHT', 'HIT_LIGHT', 'HIT_LIGHT'], -9],
    ['Tuyere', ['BEND', 'BEND'], 14],
    ['Lamp', ['DRAW', 'BEND', 'BEND'], -1],
    ['Trapdoor', ['DRAW', 'DRAW', 'BEND'], -23],
    ['Pickaxe', ['DRAW', 'BEND', 'PUNCH'], -6],
    ['Shovel', ['HIT_LIGHT', 'PUNCH'], -3],
    ['Axe', ['UPSET', 'HIT_LIGHT', 'PUNCH'], 12],
    ['Hoe', ['BEND', 'HIT_LIGHT', 'PUNCH'], 6],
    ['Hammer', ['SHRINK', 'PUNCH'], 18],
    ['Propick', ['BEND', 'DRAW', 'PUNCH'], -6],
    ['Saw', ['HIT_LIGHT', 'HIT_LIGHT'], -6],
    ['Sword', ['BEND', 'BEND', 'HIT_LIGHT'], 11],
    ['Mace', ['BEND', 'SHRINK', 'HIT_LIGHT'], 20],
    ['Scythe', ['BEND', 'DRAW', 'HIT_LIGHT'], -11],
    ['Knife', ['DRAW', 'DRAW', 'HIT_LIGHT'], -33],
    ['Javalin', ['DRAW', 'HIT_LIGHT', 'HIT_LIGHT'], -21],
    ['Chisel', ['DRAW', 'HIT_LIGHT', 'HIT_LIGHT'], -21],
    ['Helmet', ['BEND', 'BEND', 'HIT_LIGHT'], 11],
    ['Chestplate', ['UPSET', 'HIT_LIGHT', 'HIT_LIGHT'], 7],
    ['Greaves', ['HIT_LIGHT', 'DRAW', 'BEND'], -11],
    ['Boots', ['SHRINK', 'BEND', 'BEND'], 30],
    ['Shield', ['BEND', 'BEND', 'UPSET'], 27],
    ['Ironbar', ['PUNCH', 'PUNCH', 'UPSET'], 17],
    ['Door', ['PUNCH', 'DRAW', 'HIT_LIGHT'], -16],
    ['Bucket', ['BEND', 'BEND', 'BEND', 21],
    ['Grill', ['DRAW', 'PUNCH', 'PUNCH'], -11],
    ['Mechanism', ['PUNCH', 'HIT_LIGHT', 'PUNCH'], 1],
    ['Rod', ['PUNCH', 'DRAW', 'DRAW'], -28],
    ['Refine', ['HIT_LIGHT', 'HIT_LIGHT', 'HIT_LIGHT'], -9],
    ['Split', ['PUNCH'], 2],
    ['Work', ['HIT_LIGHT', 'HIT_LIGHT', 'HIT_LIGHT'], -9],
    ['High Carbon Steel', ['HIT_LIGHT', 'HIT_LIGHT', 'HIT_LIGHT'], -9],
    ['Steel', ['HIT_LIGHT', 'HIT_LIGHT', 'HIT_LIGHT'], -9]
]

#List of modded items
moddedItems = [
    ['Crown', ['SHRINK', 'UPSET', 'HIT_LIGHT'], 26],
    ['Bracing', ['DRAW', 'HIT_LIGHT', 'BEND'], -11],
    ['Bear Trap', ['SHRINK', 'DRAW', 'HIT_LIGHT'], -2],
    ['Iron Carrot', ['BEND', 'HIT_LIGHT', 'PUNCH'], 6],
    ['Honing Steel', ['DRAW', 'HIT_LIGHT', 'SHRINK'], -2],
    ['Hook Javelin', ['BEND', 'UPSET', 'DRAW'], 5],
    ['Prohammer', ['SHRINK', 'DRAW', 'PUNCH'], 3],
    ['Long Rod', ['HIT_LIGHT', 'HIT_LIGHT', 'HIT_LIGHT'], -9],
    ['Groove', ['BEND', 'BEND', 'HIT_LIGHT'], 11],
    ['Bowl Mount', ['BEND', 'DRAW', 'BEND'], -1],
    ['Draw Plate', ['HIT_LIGHT', 'PUNCH', 'PUNCH'], 1],
    ['Tongs', ['BEND', 'DRAW', 'HIT_LIGHT'], -11],
    ['Blowpipe', ['BEND', 'BEND'], 14]
]

customItems = []        #List of user-generated items
initializedItems = []   #List of currently initialized items


class SmithingItem:
    #Used to intialize a smithing object
    #Takes an initialization value list composing of a name, rule set, and optional offset
    def __init__(self, initValue):
        self.setName(initValue[0])                  #Sets the item's name to the one in the initialization list
        self.setRuleSet(initValue[1])               #Sets the item's rule set to the one in the initialization list
        
        if initValue[2] != None:                    #If there is a given offset...
            self.setOffset(initValue[2])            #Sets the item's offset to it
        else:                                       #Else...
            self.setOffset(self.calculateOffset())  #Calculates the item's offset and sets it to that

    #Mutators
    def setName(self, tempName):        #Sets the name of the item
        self.name = tempName
        
    def setRuleSet(self, tempRuleSet):  #Sets the rule set of the item
        self.RuleSet = tempRuleSet
        
    def setOffset(self, tempOffset):    #Sets the offset of the item
        self.offset = tempOffset

    #Accessors
    def getName(self):          #Returns name of smithing object
        return self.name
    
    def getRule(self):          #Returns the rules of a smithing object
        return self.ruleSet    

    def getOffset(self):        #Returns offset of smithing object    
            return self.offset

    def addRule(self, rule):                        #Used to append rules to smithing object
        if rule.upper() in validActions.keys():     #If rule passed is valid...
            self.ruleSet.append(rule)               #Append the rule to the rule set of the item
        else:                                       #Else...
            print('Action is invalid.\n')           #Print action is invalid

    def deleteRule(self):                           #Used to pop rules off smithing object
        self.ruleSet.pop()                          #Removes the trailing rule of the item's rule set

    def calculateOffset(self):                      #Calculates offset based on smithing object rules
        for rule in self.ruleSet:                   #For each rule in item's rule set...
            offset += validActions[rule]            #Convert that rule to its value and add it to the offset
        return offset                               #Return the offset of the item


#Standard menu. Prompts for displaying list of items and actions you can take.
def main():
    initialized = False
    
    #Opens SmithingItem files for object initilization...
    if !vanillaItemsFile:                                   #If vanillaItemsFile has not been opened...
        vanillaItemsFile = open('vanillaItems.bin', 'r+b')  #Open vanillaItemsFile for read/write in binary mode
    if !customItemsFile:                                    #If customItemsFile has not been opened...
        customItemsFile = open('customItems.bin', 'r+b')    #Open customItemsFile for read/write in binary mode
    if !moddedItemsFile:                                    #If moddedItemsFile has not been opened...
        moddedItemsFile = open('moddedItems.bin', 'r+b')    #Open customItemsFile for read/write in binary mode

    #Initialize SmithingItems
    if !initialized:        #If not initialized...
        initializeItems()   #Initialize all smithing items
        initialized = True  #Set initialized to true

    while True:                                                                 #While program is running...
        userChoice = input('What would you like to do? \n\
                            <<<ENTER OPTIONS TO SEE AVAILABLE OPTIONS>>> \n')   #Prompt user for input
        if userChoice in menu.keys():                                           #If a valid input...
            menu[userChoice]                                                    #Execute that input
        else:                                                                   #Else...
            print('\nPlease enter a valid choice.\n')                           #Reprompt
            
        
#Loads initialization values and initializes objects
def initializeItems():
    initializeItems.clear()             #Clears previously initialized items
    for initValue in vanillaItems:      #For each initialization list in registered vanilla items...
        obj = smithingItem(initValue)   #Initialize that item
        initializedItems.append(obj)    #Append to initialized items
    for initValue in moddedItems:       #For each initialization list in registered modded items...
        obj = smithingItem(initValue)   #Initialize that item
        initializedItems.append(obj)    #Append to initialized items
    for initValue in customItems:       #For each initialization list in registered custom items...
        obj = smithingItem(initValue)   #Initialize that item
        initializedItems.append(obj)    #Append to initialized items

#Calculate actions for the smith using targetValue and SmithingItem offset
def calculateSmith(targetValue, offset):
    target = targetValue + offset
    return smithActions

def getTarget():
    return targetValue
    
#Performs smith
def performSmith():
    userChoice = input('What item would you like to smith? \n\
                        <<<ENTER LIST TO SEE AVAILABLE ITEMS>>> \n').upper()
    if userChoice == 'LIST':
        listOptions()
        
    else if userChoice in initializedItems.keys():
        while True:
            confirmation = input('Are you ready to smith? Y/N').upper()
                if confirm(confirmation):
                    targetValue = getTarget()
                    calculateSmith(targetValue)

def confirm(userChoice):
    while True:                                                                             #Until user enters a valid choice...
        if (userChoice == 'Y') or (userChoice == 'YES'):                                        #If user chooses a variant of 'yes'...
            return True                                                                     #Return true
        else if (userChoice == 'N') or (userChoice == 'NO'):                                   #Else if user chooses a variant of 'no'...
            while True:                                                                     #Until user enters a valid choice...
                exitOption = input('Do you want to return back to the menu? Y/N').upper()   #Prompt user if they want to return to the main menu
                if (exitOption == 'Y') or (exitOption == 'YES'):                                #If user chooses a variant of 'yes'...
                    main()                                                                  #Return to main menu
                else if (exitOption == 'N') or (exitOption == 'NO'):                            #If user chooses a variant of 'no'...
                    return False                                                            #Return false
                else:                                                                       #Else...
                    print('Please enter a valid choice.\n')                                 #Prompt user to enter a valid input
        else:                                                                               #Else...
            print('Please enter a valid choice.\n')                                         #Prompt user to enter a valid input
            
            

#Regenerates the SmithingItem files
#Make a custom SmithingItem file for custom smithing items? 
def regenerateFile():
    print('-------------------------------------')  #Warns user
    print('|           !!!WARNING!!!           |')
    print('|   Regenerating these files will   |')
    print('|   cause all changes made to reset |')
    print('-------------------------------------')
    userChoice = input('Would you like to regenerate vanilla, modded, or all files? \
                        Choices include: vanilla, modded, all \n\
                        ***Enter nothing to escape***').lower() #Prompts user which file they want to regenerate
    
    while (userChoice != ''):
        if (userChoice == 'vanilla'):                             #If the user chooses to regenerate vanilla file...
                pickle.dump(vanillaItems, vanillaItemsFile)     #Regenerate vanilla file
                
        else if (userChoice == 'modded'):                         #If the user chooses to regenerate modded file...
                pickle.dump(moddedItems, moddedItemsFile)       #Regenerate modded file
                
        else if (userChoice == 'all'):                            #If the user chooses to regenerate all files...
                pickle.dump(vanillaItems, vanillaItemsFile)     #Regenerate vanilla file
                pickle.dump(moddedItems, moddedItemsFile)       #Regenerate modded file
                
        else:                                                   #Else...
            userChoice = input('That is not a valid option. \
                Please re-enter your choice.').lower()          #Prompt user to re-enter their choice

def reloadFile():
    vanillaItems.clear()                                          #Erase current loaded vanilla items
    moddedItems.clear()                                           #Erase current loaded modded items
    vanillaItems = pickle.load(vanillaItemsFile)                  #Load vanilla items from file
    moddedItems = pickle.load(moddedItemsFile)                    #Load modded items from file

    userChoice = input('\nReinitialize items? Y/N: ').upper()     #Prompt user for reinitialization
    if confirm(userChoice):
        initializeItems()

def createSmithingItem():
    name = input('\nWhat do you want the item\'s name to be?: ')#Prompts for item's name

    ruleSet = []                                                #Initializes rule set to be added
    while (userChoice != ''):                                     #While the user does not end prompt...
        userChoice = input('\nInput nothing to end rule set. \
            Input action rules from initial to last:\n').upper()#Prompt the user for a rule to be added. Puts it in uppercase.
        if userChoice in validActions.keys():                   #If the rule the user entered is valid...
            ruleSet.append(userChoice)                          #Append the rule to the ruleset
        else:
            print('\nPlease input a proper action rule.\n')     #Else prompt user for a proper rule

    offset = None                                               #Set default offset to None                            
    offset = input('\nEnter a custom offset or enter nothing \
        to calculate default: ')                                #Prompt the user for an offset

    obj = SmithingItem(name, ruleSet, offset)
    values = [name, ruleSet, offset]
    initializedItems.append(values)
    moddedItems.append(values)

def modifySmithingItem():
    userChoice = input('What item would you like to modify? \
                        <<<ENTER LIST FOR AVAILABLE ITEMS>>> \n').upper()
    
    if (userChoice == 'LIST'):
        listSmithingItems()

    for item in initializedItems:
        if (userChoice == item[0]):
            print('Objects attributes include:\n\
                   Name: ' + item[0] + '\n\
                   Rule Set: ' + item[1] + '\n\
                   Offset: ' + item[2] + '\n')
            userModify == input('Which would you like to modify? NAME/RULE SET/OFFSET').upper()
            if (userModify == 'NAME'):
                name = input('Enter a new name: ').capitalize()
                item[0] = name
            else if (userModify == 'RULE SET'):
                
            
        else:
            print('

def listSmithingItems():
    print('Current smithable items include: \n')
    for item in initializedItems:
        print(item[0] + ', ')
    print('\n')

def listOptions():
    print('Available options include: \n\
           LIST (List smithable items) \n\
           SMITH (Smith chosen item) \n\
           CREATE (Create custom smithable item) \n\
           MODIFY (Modify existing smithable item) \n\
           INITIALIZE (Initialize smithable items) \n\
           RELOAD (Reload smithable items) \n\
           REGENERATE (Regenerate smithing item files) \n')

def terminateProgram():
    vanillaItemsFile.close()
    moddedItemsFile.close()
    customItemsFile.close()
    exit()
    

    
