import pyautogui

gridToCoordinates = [
    [(825, 388), (860, 388), (888, 388), (920, 388), (950, 388)],
    [(825, 420), (860, 420), (888, 420), (920, 420), (950, 420)],
    [(825, 450), (860, 450), (888, 450), (920, 450), (950, 450)],
    [(825, 488), (860, 488), (888, 488), (920, 488), (950, 488)],
    [(825, 515), (860, 515), (888, 515), (920, 515), (950, 515)],
]

knappedAxe = [gridToCoordinates[0][0], gridToCoordinates[0][2], gridToCoordinates[0][3], gridToCoordinates[0][4],
              gridToCoordinates[1][4],
              gridToCoordinates[3][4],
              gridToCoordinates[4][0], gridToCoordinates[4][2], gridToCoordinates[4][3], gridToCoordinates[4][4]
              ]

knappedShovel = [gridToCoordinates[0][0], gridToCoordinates[0][4],
                 gridToCoordinates[1][0], gridToCoordinates[1][4],
                 gridToCoordinates[2][0], gridToCoordinates[2][4],
                 gridToCoordinates[3][0], gridToCoordinates[3][4],
                 gridToCoordinates[4][0], gridToCoordinates[4][1], gridToCoordinates[4][3], gridToCoordinates[4][4]
                 ]

knappedHoe = [gridToCoordinates[1][0], gridToCoordinates[1][1], gridToCoordinates[1][3],
              gridToCoordinates[2][0], gridToCoordinates[2][1], gridToCoordinates[2][2], gridToCoordinates[2][3], gridToCoordinates[2][4],
              gridToCoordinates[4][0], gridToCoordinates[4][1], gridToCoordinates[4][2]
              ]

knappedJavelin = [gridToCoordinates[0][3], gridToCoordinates[0][4],
                  gridToCoordinates[1][4],
                  gridToCoordinates[3][0], gridToCoordinates[3][4],
                  gridToCoordinates[4][0], gridToCoordinates[4][1], gridToCoordinates[4][3], gridToCoordinates[4][4]
                  ]

knappedHammer = [gridToCoordinates[2][0], gridToCoordinates[2][1], gridToCoordinates[2][3], gridToCoordinates[2][4],
                 gridToCoordinates[3][0], gridToCoordinates[3][1], gridToCoordinates[3][2], gridToCoordinates[3][3], gridToCoordinates[3][4],
                 gridToCoordinates[4][0], gridToCoordinates[4][1], gridToCoordinates[4][2], gridToCoordinates[4][3], gridToCoordinates[4][4]
                 ]

knappedKnife = [gridToCoordinates[0][1], gridToCoordinates[0][2], gridToCoordinates[0][4],
                gridToCoordinates[1][2],
                gridToCoordinates[2][2],
                gridToCoordinates[3][2],
                gridToCoordinates[4][2]
                ]

moldedIngot = [gridToCoordinates[1][1], gridToCoordinates[1][2],
               gridToCoordinates[2][1], gridToCoordinates[2][2],
               gridToCoordinates[3][1], gridToCoordinates[3][2]
               ]

moldedPickaxe = [gridToCoordinates[1][1], gridToCoordinates[1][2], gridToCoordinates[1][3],
                 gridToCoordinates[2][0], gridToCoordinates[2][4]
                 ]

moldedShovel = [gridToCoordinates[0][1], gridToCoordinates[0][2], gridToCoordinates[0][3],
                gridToCoordinates[1][1], gridToCoordinates[1][2], gridToCoordinates[1][3],
                gridToCoordinates[2][1], gridToCoordinates[2][2], gridToCoordinates[2][3],
                gridToCoordinates[3][1], gridToCoordinates[3][2], gridToCoordinates[3][3],
                gridToCoordinates[4][2]
                ]
moldedAxe = [gridToCoordinates[0][1],
             gridToCoordinates[1][0], gridToCoordinates[1][1], gridToCoordinates[1][2], gridToCoordinates[1][3],
             gridToCoordinates[2][0], gridToCoordinates[2][1], gridToCoordinates[2][2], gridToCoordinates[2][3], gridToCoordinates[2][4],
             gridToCoordinates[3][0], gridToCoordinates[3][1], gridToCoordinates[3][2], gridToCoordinates[3][3],
             gridToCoordinates[4][0]
             ]

moldedHoe = [gridToCoordinates[1][0], gridToCoordinates[1][1], gridToCoordinates[1][2], gridToCoordinates[1][3], gridToCoordinates[1][4],
             gridToCoordinates[2][0], gridToCoordinates[2][1]
             ]

moldedChisel = [gridToCoordinates[0][2],
                gridToCoordinates[1][2],
                gridToCoordinates[2][2],
                gridToCoordinates[3][2],
                gridToCoordinates[4][2]
                ]

moldedSword = [gridToCoordinates[0][3], gridToCoordinates[0][4],
               gridToCoordinates[1][2], gridToCoordinates[1][3], gridToCoordinates[1][4],
               gridToCoordinates[2][1], gridToCoordinates[2][2], gridToCoordinates[2][3],
               gridToCoordinates[3][1], gridToCoordinates[3][2],
               gridToCoordinates[4][0]
               ]

moldedMace = [gridToCoordinates[0][2],
              gridToCoordinates[1][1], gridToCoordinates[1][2], gridToCoordinates[1][3],
              gridToCoordinates[2][1], gridToCoordinates[2][2], gridToCoordinates[2][3],
              gridToCoordinates[3][1], gridToCoordinates[3][2], gridToCoordinates[3][3],
              gridToCoordinates[4][2]
              ]

moldedSaw = [gridToCoordinates[0][3], gridToCoordinates[0][4],
             gridToCoordinates[1][2], gridToCoordinates[1][3], gridToCoordinates[1][4],
             gridToCoordinates[2][1], gridToCoordinates[2][2], gridToCoordinates[2][3],
             gridToCoordinates[3][0], gridToCoordinates[3][1], gridToCoordinates[3][2], gridToCoordinates[3][3],
             gridToCoordinates[4][0], gridToCoordinates[4][1]
             ]

moldedJavelin = [gridToCoordinates[0][2], gridToCoordinates[0][3], gridToCoordinates[0][4],
                 gridToCoordinates[1][1], gridToCoordinates[1][2], gridToCoordinates[1][3], gridToCoordinates[1][4],
                 gridToCoordinates[2][0], gridToCoordinates[2][1], gridToCoordinates[2][2], gridToCoordinates[2][3], gridToCoordinates[2][4],
                 gridToCoordinates[3][1], gridToCoordinates[3][2], gridToCoordinates[3][3],
                 gridToCoordinates[4][2]
                 ]

moldedHammer = [gridToCoordinates[1][0], gridToCoordinates[1][1], gridToCoordinates[1][2], gridToCoordinates[1][3], gridToCoordinates[1][4],
                gridToCoordinates[2][0], gridToCoordinates[2][1], gridToCoordinates[2][2], gridToCoordinates[2][3], gridToCoordinates[2][4],
                gridToCoordinates[3][2]
                ]

moldedPropick = [gridToCoordinates[1][0], gridToCoordinates[1][1], gridToCoordinates[1][2], gridToCoordinates[1][3],
                 gridToCoordinates[2][0], gridToCoordinates[2][4],
                 gridToCoordinates[3][0]
                 ]

moldedKnife = [gridToCoordinates[0][2],
               gridToCoordinates[1][2], gridToCoordinates[1][3],
               gridToCoordinates[2][2], gridToCoordinates[2][3],
               gridToCoordinates[3][2], gridToCoordinates[3][3],
               gridToCoordinates[4][2], gridToCoordinates[4][3]
               ]

moldedScythe = [gridToCoordinates[1][1], gridToCoordinates[1][2], gridToCoordinates[1][3], gridToCoordinates[1][4],
                gridToCoordinates[2][0], gridToCoordinates[2][1], gridToCoordinates[2][2], gridToCoordinates[2][3],
                gridToCoordinates[3][0], gridToCoordinates[3][1]
                ]

moldedLargevessel = [gridToCoordinates[0][1], gridToCoordinates[0][2], gridToCoordinates[0][2],
                     gridToCoordinates[1][1], gridToCoordinates[1][2], gridToCoordinates[1][2],
                     gridToCoordinates[2][1], gridToCoordinates[2][2], gridToCoordinates[2][2],
                     gridToCoordinates[3][1], gridToCoordinates[3][2], gridToCoordinates[3][2]
                     ]

moldedSmallvessel = [gridToCoordinates[0][0], gridToCoordinates[0][4],
                     gridToCoordinates[4][0], gridToCoordinates[4][4]
                     ]

moldedPot = [gridToCoordinates[0][1], gridToCoordinates[0][2], gridToCoordinates[0][3],
             gridToCoordinates[1][1], gridToCoordinates[1][2], gridToCoordinates[1][3],
             gridToCoordinates[2][1], gridToCoordinates[2][2], gridToCoordinates[2][3],
             gridToCoordinates[4][0], gridToCoordinates[4][4]
             ]

moldedBowl = [gridToCoordinates[0][1], gridToCoordinates[0][2], gridToCoordinates[0][3],
              gridToCoordinates[1][0], gridToCoordinates[1][4],
              gridToCoordinates[2][0], gridToCoordinates[2][1], gridToCoordinates[2][2], gridToCoordinates[2][3], gridToCoordinates[2][4],
              gridToCoordinates[3][1], gridToCoordinates[3][2], gridToCoordinates[3][3],
              gridToCoordinates[4][0], gridToCoordinates[4][4]
              ]

moldedJug = [gridToCoordinates[0][0], gridToCoordinates[0][2], gridToCoordinates[0][3], gridToCoordinates[0][4],
             gridToCoordinates[1][4],
             gridToCoordinates[2][3],
             gridToCoordinates[3][4],
             gridToCoordinates[4][3], gridToCoordinates[4][4]
             ]

moldedMug = [gridToCoordinates[0][0], gridToCoordinates[0][1], gridToCoordinates[0][2], gridToCoordinates[0][3], gridToCoordinates[0][4],
             gridToCoordinates[1][4],
             gridToCoordinates[2][3],
             gridToCoordinates[3][4],
             gridToCoordinates[4][3], gridToCoordinates[4][4]
             ]

moldedSleeve = [gridToCoordinates[1][2],
                gridToCoordinates[2][1], gridToCoordinates[2][3],
                gridToCoordinates[3][2]
                ]

moldedRackwheel = [gridToCoordinates[1][1],
                   gridToCoordinates[2][1], gridToCoordinates[2][2],
                   gridToCoordinates[3][2], gridToCoordinates[3][3]
                   ]

moldedGlassblock = [gridToCoordinates[0][1], gridToCoordinates[0][2], gridToCoordinates[0][3],
                    gridToCoordinates[1][1], gridToCoordinates[1][2], gridToCoordinates[1][3],
                    gridToCoordinates[2][1], gridToCoordinates[2][2], gridToCoordinates[2][3],
                    gridToCoordinates[3][1], gridToCoordinates[3][2], gridToCoordinates[3][3],
                    gridToCoordinates[4][0], gridToCoordinates[4][4]
                    ]

moldedGlasspane = [gridToCoordinates[1][1], gridToCoordinates[1][2], gridToCoordinates[1][3],
                   gridToCoordinates[2][1], gridToCoordinates[2][2], gridToCoordinates[2][3],
                   gridToCoordinates[3][1], gridToCoordinates[3][2], gridToCoordinates[3][3]
                   ]

userItemToItem = {
    'knappedAxe'        : knappedAxe,
    'knappedShovel'     : knappedShovel,
    'knappedHoe'        : knappedHoe,
    'knappedJavelin'    : knappedJavelin,
    'knappedHammer'     : knappedHammer,
    'knappedKnife'      : knappedKnife,
    'moldedIngot'       : moldedIngot,
    'moldedPickaxe'     : moldedPickaxe,
    'moldedShovel'      : moldedShovel,
    'moldedAxe'         : moldedAxe,
    'moldedHoe'         : moldedHoe,
    'moldedChisel'      : moldedChisel,
    'moldedSword'       : moldedSword,
    'moldedMace'        : moldedMace,
    'moldedSaw'         : moldedSaw,
    'moldedJavelin'     : moldedJavelin,
    'moldedHammer'      : moldedHammer,
    'moldedPropick'     : moldedPropick,
    'moldedKnife'       : moldedKnife,
    'moldedScythe'      : moldedScythe,
    'moldedLargevessel' : moldedLargevessel,
    'moldedSmallvessel' : moldedSmallvessel,
    'moldedPot'         : moldedPot,
    'moldedBowl'        : moldedBowl,
    'moldedJug'         : moldedJug,
    'moldedMug'         : moldedMug,
    'moldedSleeve'      : moldedSleeve,
    'moldedRackwheel'   : moldedRackwheel,
    'moldedGlassblock'  : moldedGlassblock,
    'moldedGlasspane'   : moldedGlasspane
    }

#mousePosition = pyautogui.position()
#print(mousePosition)
#pyautogui.moveTo(2834, 610)
#print(str(gridToCoordinates[0][1]))
#test = input()

knappedItem = 'Axe, Shovel, Hoe, Javelin, Hammer, Knife'
moldedItem = 'Ingot, Pickaxe, Chisel, Sword, Mace, Saw, Propick, Scythe, LargeVessel, SmallVessel, Pot, Bowl, Jug, Mug, Sleeve, RackWheel, GlassBlock, GlassPane'
moldedItem = knappedItem + ', ' + moldedItem
moldedItemArray = list(moldedItem.split(", "))
knappedItemArray = list(knappedItem.split(", "))
userItem = ''

while True:
    print('Would you like to knap or mold?')
    userKnapOrMold = input()
    userKnapOrMold = userKnapOrMold.upper()
    if userKnapOrMold != 'KNAP' and userKnapOrMold != 'MOLD':
        print('\nPlease enter a valid response.\n')
    elif userKnapOrMold == 'KNAP':
        while True:
            print('\nWhat would you like to knap?')
            userItem = input('<<<ENTER LIST FOR OPTIONS>>>\n')
            userItem = userItem.capitalize()
            if knappedItemArray.count(userItem) < 0 and userItem != 'List':
                print('\nPlease enter a valid item.\n')
            elif userItem == 'List':
                print('\nPossible options include: ' + knappedItem)
            else:
                userItem = 'knapped' + userItem
                print('\nHow many would you like to make?')
                userAmount = input()
                print('Operation will cost: ' + str(int(userAmount)) + ' rock.') 
                while True:
                    userConfirmation = input('Are you ready to ' + userKnapOrMold.lower() + '? Y/N\n')
                    userConfirmation = userConfirmation.upper()
                    if userConfirmation == 'Y' or userConfirmation == 'YES':
                        break
                    elif userConfirmation == 'N' or userConfirmation == 'NO':
                        exit()
                    else:
                        print('Please input a valid response.\n')
                pyautogui.moveTo(900, 500)
                pyautogui.click(button='right')
                for i in range(int(userAmount)):
                    for counter, value in enumerate(userItemToItem[userItem]):
                        pyautogui.moveTo(value)
                        pyautogui.click()
                    pyautogui.press('esc')
                    pyautogui.click(button='right')
                print('\nDone!\n')
                break
            
    elif userKnapOrMold == 'MOLD':
        while True:
            print('\nWhat would you like to mold?')
            userItem = input('<<<ENTER LIST FOR OPTIONS>>>\n')
            userItem = userItem.capitalize()
            if moldedItemArray.count(userItem) < 0 and userItem != 'List':
                print('\nPlease enter a valid item.\n')
            elif userItem == 'List':
                print('\nPossible options include: ' + moldedItem)
            else:
                userItem = 'molded' + userItem
                print('\nHow many would you like to make?')
                userAmount = input()
                print('Operation will cost: ' + str(int(userAmount) * 5) + ' clay.') 
                while True:
                    userConfirmation = input('Are you ready to ' + userKnapOrMold.lower() + '? Y/N\n')
                    userConfirmation = userConfirmation.upper()
                    if userConfirmation == 'Y' or userConfirmation == 'YES':
                        break
                    elif userConfirmation == 'N' or userConfirmation == 'NO':
                        exit()
                    else:
                        print('Please input a valid response.\n')
                pyautogui.moveTo(900, 500)
                pyautogui.click(button='right')
                for i in range(int(userAmount)):
                    for counter, value in enumerate(userItemToItem[userItem]):
                        pyautogui.moveTo(value)
                        pyautogui.click()
                    pyautogui.press('esc')
                    pyautogui.click(button='right')
                print('\nDone!\n')
                break
              
        

























