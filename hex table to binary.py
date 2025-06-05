fileIn = open("hexfile.txt", 'r')                                       #Opens file containing hex for reading
fileOut = open("binaryfile.txt", 'w')                                   #Opens file to write to
hexinput = fileIn.read()                                                #Reads hex data into hexinput
hexinput = hexinput.split()                                             #Splits hex data into list based on whitespace
for index, value in enumerate(hexinput):                                #Enumerates hexinput and for each element in hexinput:
    hexinput[index] = str(bin(int('0x' + hexinput[index], 16)))         #Appends 0x to each hex number, converts to integer, then to binary, then puts binary in string form
    hexinput[index] = hexinput[index][2:]                               #Strips 0b from binary number    
    hexinput[index] = hexinput[index].rjust(8, '0')                     #Pads binary number to make a byte (8 bits)
hexstring = str(hexinput)                                               #Takes array of string binary and puts it as one string
hexstring = hexstring.translate(hexstring.maketrans('', '', "[],'"))    #Converts string to translation table to remove array characters
fileOut.write(hexstring)                                                #Writes binary numbers to file


