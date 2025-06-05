from PIL import Image
import pyautogui
import time

#List of the actions that must be completed for the item to be made. The "Action Rules".
#Modded items

ruleItemToAction = {
#Modded items
'ruleCrownAction' : ['SHRINK', 'UPSET', 'HIT_LIGHT'],
'ruleBracingAction' : ['DRAW', 'HIT_LIGHT', 'BEND'],
'ruleBearTrapAction' : ['SHRINK', 'DRAW', 'HIT_LIGHT'],
'ruleIronCarrotAction' : ['BEND', 'HIT_LIGHT', 'PUNCH'],
'ruleHoningSteelAction' : ['DRAW', 'HIT_LIGHT', 'SHRINK'],
'ruleHookJavelinAction' : ['BEND', 'UPSET', 'DRAW'],
'ruleProhammerAction' : ['SHRINK', 'DRAW', 'PUNCH'],
'ruleLongRodAction' : ['HIT_LIGHT', 'HIT_LIGHT', 'HIT_LIGHT'],
'ruleGrooveAction' : ['BEND', 'BEND', 'HIT_LIGHT'],
'ruleBowlMountAction' : ['BEND', 'DRAW', 'BEND'],
'ruleDrawPlateAction' : ['HIT_LIGHT', 'PUNCH', 'PUNCH'],
'ruleTongsAction' : ['BEND', 'DRAW', 'HIT_LIGHT'],
'ruleBlowpipeAction' : ['BEND', 'BEND'],
#Vanilla items
'ruleSheetAction' : ['HIT_LIGHT', 'HIT_LIGHT', 'HIT_LIGHT'],
'ruleTuyereAction' : ['BEND', 'BEND'],
'ruleLampAction' : ['DRAW', 'BEND', 'BEND'],
'ruleTrapdoorAction' : ['DRAW', 'DRAW', 'BEND'],
'rulePickaxeAction' : ['DRAW', 'BEND', 'PUNCH'],
'ruleShovelAction' : ['HIT_LIGHT', 'PUNCH'],
'ruleAxeAction' : ['UPSET', 'HIT_LIGHT', 'PUNCH'],
'ruleHoeAction' : ['BEND', 'HIT_LIGHT', 'PUNCH'],
'ruleHammerAction' : ['SHRINK', 'PUNCH'],
'rulePropickAction' : ['BEND', 'DRAW', 'PUNCH'],
'ruleSawAction' : ['HIT_LIGHT', 'HIT_LIGHT'],
'ruleSwordAction' : ['BEND', 'BEND', 'HIT_LIGHT'],
'ruleMaceAction' : ['BEND', 'SHRINK', 'HIT_LIGHT'],
'ruleScytheAction' : ['BEND', 'DRAW', 'HIT_LIGHT'],
'ruleKnifeAction' : ['DRAW', 'DRAW', 'HIT_LIGHT'],
'ruleJavelinAction' : ['DRAW', 'HIT_LIGHT', 'HIT_LIGHT'],
'ruleChiselAction' : ['DRAW', 'HIT_LIGHT', 'HIT_LIGHT'],
'ruleHelmetAction' : ['BEND', 'BEND', 'HIT_LIGHT'],
'ruleChestplateAction' : ['UPSET', 'HIT_LIGHT', 'HIT_LIGHT'],
'ruleGreavesAction' : ['HIT_LIGHT', 'DRAW', 'BEND'],
'ruleBootsAction' : ['SHRINK', 'BEND', 'BEND'],
'ruleShieldAction' : ['BEND', 'BEND', 'UPSET'],
'ruleIronbarAction' : ['PUNCH', 'PUNCH', 'UPSET'],
'ruleDoorAction' : ['PUNCH', 'DRAW', 'HIT_LIGHT'],
'ruleBucketAction' : ['BEND', 'BEND', 'BEND'],
'ruleGrillAction' : ['DRAW', 'PUNCH', 'PUNCH'],
'ruleMechanismAction' : ['PUNCH', 'HIT_LIGHT', 'PUNCH'],
'ruleRodAction' : ['PUNCH', 'DRAW', 'DRAW'],
'ruleRefineAction' : ['HIT_LIGHT', 'HIT_LIGHT', 'HIT_LIGHT'],
'ruleSplitAction' : ['PUNCH'],
'ruleWorkAction' : ['HIT_LIGHT', 'HIT_LIGHT', 'HIT_LIGHT'],
'ruleHighCarbonSteelAction' : ['HIT_LIGHT', 'HIT_LIGHT', 'HIT_LIGHT'],
'ruleSteelAction' : ['HIT_LIGHT', 'HIT_LIGHT', 'HIT_LIGHT']
#User Added Items
}

#The list of valid smithingItems and their respective action rules.
smithingItem = {
                 #TFCThings Mod
                 'CROWN'          : ruleItemToAction['ruleCrownAction'],
                 'BRACING'        : ruleItemToAction['ruleBracingAction'],
                 'BEARTRAP'       : ruleItemToAction['ruleBearTrapAction'],
                 'IRONCARROT'     : ruleItemToAction['ruleIronCarrotAction'],
                 'HONINGSTEEL'    : ruleItemToAction['ruleHoningSteelAction'],
                 'HOOKJAVELIN'    : ruleItemToAction['ruleHookJavelinAction'],
                 #TFCTech Mod
                 'PROHAMMER'      : ruleItemToAction['ruleProhammerAction'],
                 'LONGROD'        : ruleItemToAction['ruleLongRodAction'],
                 'GROOVE'         : ruleItemToAction['ruleGrooveAction'],
                 'BOWLMOUNT'      : ruleItemToAction['ruleBowlMountAction'],
                 'DRAWPLATE'      : ruleItemToAction['ruleDrawPlateAction'],
                 'TONGS'          : ruleItemToAction['ruleTongsAction'],
                 'BLOWPIPE'       : ruleItemToAction['ruleBlowpipeAction'],
                 #Vanilla
                 'SHEET'          : ruleItemToAction['ruleSheetAction'],
                 'TUYERE'         : ruleItemToAction['ruleTuyereAction'],
                 'LAMP'           : ruleItemToAction['ruleLampAction'],
                 'TRAPDOOR'       : ruleItemToAction['ruleTrapdoorAction'],
                 'PICKAXE'        : ruleItemToAction['rulePickaxeAction'],
                 'SHOVEL'         : ruleItemToAction['ruleShovelAction'],
                 'AXE'            : ruleItemToAction['ruleAxeAction'],
                 'HOE'            : ruleItemToAction['ruleHoeAction'],
                 'HAMMER'         : ruleItemToAction['ruleHammerAction'],
                 'PROPICK'        : ruleItemToAction['rulePropickAction'],
                 'SAW'            : ruleItemToAction['ruleSawAction'],
                 'SWORD'          : ruleItemToAction['ruleSwordAction'],
                 'MACE'           : ruleItemToAction['ruleMaceAction'],
                 'SCYTHE'         : ruleItemToAction['ruleScytheAction'],
                 'KNIFE'          : ruleItemToAction['ruleKnifeAction'],
                 'JAVELIN'        : ruleItemToAction['ruleJavelinAction'],
                 'CHISEL'         : ruleItemToAction['ruleChiselAction'],
                 'HELMET'         : ruleItemToAction['ruleHelmetAction'],
                 'CHESTPLATE'     : ruleItemToAction['ruleChestplateAction'],
                 'GREAVES'        : ruleItemToAction['ruleGreavesAction'],
                 'BOOTS'          : ruleItemToAction['ruleBootsAction'],
                 'SHIELD'         : ruleItemToAction['ruleShieldAction'],
                 'IRONBAR'        : ruleItemToAction['ruleIronbarAction'],
                 'DOOR'           : ruleItemToAction['ruleDoorAction'],
                 'BUCKET'         : ruleItemToAction['ruleBucketAction'],
                 'GRILL'          : ruleItemToAction['ruleGrillAction'],
                 'MECHANISM'      : ruleItemToAction['ruleMechanismAction'],
                 'ROD'            : ruleItemToAction['ruleRodAction'],
                 'REFINE'         : ruleItemToAction['ruleRefineAction'],
                 'SPLIT'          : ruleItemToAction['ruleSplitAction'],
                 'WORK'           : ruleItemToAction['ruleWorkAction'],
                 'HIGHCARBONSTEEL': ruleItemToAction['ruleHighCarbonSteelAction'],
                 'STEEL'          : ruleItemToAction['ruleSteelAction']
                 #User Added items
}

#A dictionary mapping the amount of pixels the marker moves per action
valueToAction = {
    16 : 'SHRINK',
    13 : 'UPSET',
    7  : 'BEND',
    2  : 'PUNCH',
    -3 : 'HIT_LIGHT',
    -6 : 'HIT_MEDIUM',
    -9 : 'HIT_HARD',
    -15: 'DRAW'
}

#A dictionary mapping actions to the amount of pixels the mareker moves
actionToValue = {
    'SHRINK'    : 16,
    'UPSET'     : 13,
    'BEND'      : 7,
    'PUNCH'     : 2,
    'HIT_LIGHT' : -3,
    'HIT_MEDIUM': -6,
    'HIT_HARD'  : -9,
    'DRAW'      : -15,
}

#A dictionary mapping actions to the pixel location of the button for that action
actionToCoordinate = {
    'SHRINK'    : [1013,491],
    'UPSET'     : [977,491],
    'BEND'      : [1013,455],
    'PUNCH'     : [977,455],
    'HIT_LIGHT' : [907,455],
    'HIT_MEDIUM': [946,455],
    'HIT_HARD'  : [907,491],
    'DRAW'      : [946,491]
}

print('|-------------------------------------|')
print('|TFC Anvil Cheater v1.3 by ravenousdox|')
print('|-------------------------------------|\n')

while True:
    while True:
        smithingValue=[]
        smithingKey=[]
        ruleValue = []
        userRuleKeyValue = []
        userItem = ''
        userAction = 0

        print('What kind of item would you like to smith?')
        userItem = input('<<<ENTER LIST FOR OPTIONS>>>\n') #Asks user what item they want to smith
        userItem = userItem.upper() #Makes input case-insensitive 
        if userItem == 'LIST': #If the user enters 'list', the program retrieves the keys in smithingItems and creates a list, capitalizing each of the keys.
            validItem = [x.capitalize() for x in smithingItem.keys()] 
            print('\nAvailable options include: \n' + str(', '.join(validItem)) + '\n\nADD/CHANGE/REMOVE\n') #Displays the list as a string of items with a comma and space inbetween each entry
        
        elif userItem =='ADD': #If user enters 'add', the program prompts the user with what the name of the item they are adding is and formats the name to the dictionary's standard 
            userKey = input('\nInput the name of the item:\n')
            userRuleKeyAction = "'rule" + userKey.capitalize() + "Action'"
            #print('Key is: ' + userRuleKeyAction)
            while userAction != '': #Prompts the user to input the different rule actions for the item
                userAction = input('\nInput nothing to end rule set. Input action rules from initial to last:\n') #later make sure action entered is valid by checking keys in actionToValue
                userAction = userAction.upper()
                try: #Checks to see if rule action exists, if it doesn't, then the program handles the exception
                    actionToValue[userAction]
                    userRuleKeyValue.append(userAction)
                except KeyError:
                    if userAction != '':    
                        print('\nPlease input a proper action rule.')
            userKey = "'" + userKey.upper() + "'"
            userRuleActions = 'ruleItemToAction[' + userRuleKeyAction + ']'
            print('This will add entries:\n' + userKey + ' : ' + str(userRuleActions) + '\n' + userRuleKeyAction + ' : ' + str(userRuleKeyValue) + '\n') #Lists the entries to be added
            while True:
                userConfirmation = input('Are you sure? Y/N\n') #Prompts user if they want to add the entries
                userConfirmation = userConfirmation.upper()
                if userConfirmation == 'Y' or userConfirmation == 'YES':
                    userKey = userKey.upper()
                    smithingItem.update({userKey : userRuleActions})
                    ruleItemToAction.update({userRuleKeyAction : userRuleKeyValue})
                    userKey = "'" + userKey.upper() + "'"
                    print('\nSuccessfully updated ruleItemToAction with entry: ' + next(reversed(ruleItemToAction.keys())) + ' : ' + str(ruleItemToAction[next(reversed(ruleItemToAction.keys()))])) #Updates and accesses entries, later I may write them to a file
                    print('Successfully updated smithingItem with entry: ' + next(reversed(smithingItem.keys())) + ' : ' + str(smithingItem[next(reversed(smithingItem.keys()))]) + '\n')
                    break
                elif userConfirmation == 'N' or userConfirmation == 'NO':
                    print('\nAborted entry.\n')
                    break
                else:
                    print('Please enter a valid response.\n')
                
        else: #If user did not enter list, and instead wants to smith an item, the program checks if the user entered a valid smithingItem
            try:
                ruleAction = smithingItem[userItem] #Attempts to index userItem in smithingItems
                print('\n----------------------------------------\nInput valid!\nCalculating smithingKey for userItem ==', userItem + '...\n') #userItem exists and program begins to calculate values
                for counter, value in enumerate(ruleAction): #Creates a list of corresponding values for each action rule userItem has
                    ruleValue.append(actionToValue[ruleAction[counter]])
                ruleDisplacement = sum(ruleValue) #Finds the amount the actions would displace the marker in pixels, if they were to be done
                print('Rules are:', str(ruleAction)) 
                print('Values are:', str(ruleValue))
                print('Total displacement is:', str(ruleDisplacement))
                break
            except KeyError: #If userItem is not found in smithingItems, it prompts the user to enter again.
                print('\nPlease input a valid item.\n')
                userItem = ''

    while True: #Attempts to grab the slidebar of the anvil GUI and then find the end_marker's location
        try: 
            pyautogui.screenshot(r'D:\Users\Master\Desktop\Everything Important\examplegui\slidebar.png', region=(808,531,304,20))
            im = Image.open(r'D:\Users\Master\Desktop\Everything Important\examplegui\slidebar.png')
            pix = im.load()
            location = 6
            endMarker = 0
            while str(pix[location,0])!='(255, 0, 0)': #Checks each pixel to see if it is red. If it isn't, then it checks the pixel color 2 pixels to the right, effectively one marker value over.
                location += 2
                endMarker += 1
            break
        except IndexError: #Throws error if endMarker cannot be located
            print('\nIndexError: endMarker cannot be found!')
            while True:
                userContinue = input('Do you want to continue? Y/N\n')
                userContinue = userContinue.upper()
                if userContinue == 'Y' or userContinue == 'YES':
                    break
                elif userContinue == 'N' or userContinue == 'NO':
                    exit()
                else:
                    print('\nPlease enter a valid response.')
                    
    targetMarker = endMarker - ruleDisplacement #Compensates the targetMarker location for the amount of pixels the marker will move after userItem action rules occur
    print('endMarker is at value:', endMarker)
    print('targetMarker is at value:', targetMarker)

    numShrink = targetMarker // 16 #Calculates the amount of times each action can at maximum be performed without exceeding the target marker's value. The remainder is then passed down to the second-largest action.
    numLeft = targetMarker % 16
    numUpset = numLeft // 13
    numLeft = numLeft % 13
    numBend = numLeft // 7
    numLeft = numLeft % 7
    numPunch = numLeft // 2
    numLeft = numLeft % 2
    
    for i in range(numShrink): #Creates a list of the previously calculated values that add up to the targetMarker
        smithingValue.append(16)
    for i in range(numUpset):
        smithingValue.append(13)
    for i in range(numBend):
        smithingValue.append(7)
    for i in range(numPunch):
        smithingValue.append(2)
        
    if numLeft > 0: #If there is a remainder, which in testing is at most 1, then the sequence of actions PUNCH, PUNCH, and HIT_LIGHT are performed to bring it to 0. 
        smithingValue.append(7) #Appends the values that compensate for the remainder onto the list of values.
        smithingValue.append(-6)
        numLeft += -1

    smithingValue.extend(ruleValue)

    for counter, value in enumerate(smithingValue): #Retrieves the value in each index of the list smithingValues, passes them through the dictionary actionValues to get their string counterpart, then appends them onto the list smithingKey.
        smithingKey.append(valueToAction[smithingValue[counter]])

    print('smithingValues are', smithingValue)
    print('smithingKey is', smithingKey, '\n')

    while True: #Prompts user if they are ready for the actions in smithingKey to be performed
        performAction = input('Are you ready to smith? Y/N\n')
        performAction = performAction.upper() #Makes input case-insensitive 
        if performAction == 'Y' or performAction == 'YES':
            break
        elif performAction == 'N' or performAction == 'NO':
            exit()
        else:
            print('\nPlease enter a valid response.')

    mousePosition = pyautogui.position() #Saves current mouse position to return to after completing the actions
    for counter, value in enumerate(smithingKey): #
        pyautogui.click(actionToCoordinate[value])
    pyautogui.moveTo(mousePosition)
    pyautogui.click()

    print('\nDone!\n----------------------------------------\n')
