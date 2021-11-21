
DENARYNUM = 0
def binarytodenary(binaryNumber):
    #BINARY TO DENARY
    global DENARYNUM

    

    numBits = len(binaryNumber)
    DENARYNUM = 0 
    for bit in range(0, numBits):
        DENARYNUM = DENARYNUM + (int(binaryNumber[bit]) * 2**(numBits-1-bit))

    print("\nThe denary number is: ",DENARYNUM)
    return()

#DENARY TO BINARY 
denaryDTB = 0 
denarystore = 0 #Made new variable since denaryDTB will become 0 at the end of the loop.
def denarytobinary():
    global denaryDTB
    #denaryDTB = int(input("Enter a denary Number: ")) #input a denary
    global denarystore 
    denarystore = denaryDTB
    binary = []
    while denaryDTB != 0:
        if denaryDTB % 2 == 0: #check if modulus
            denaryDTB = denaryDTB / 2
            binary.insert(0,0) #add the binary number at a specific index and element using list and insert function
        else:
            denaryDTB = (denaryDTB - 1) / 2
            binary.insert(0,1)
    print("\nThe Binary number is:",binary)
    return

#DENARY TO HEX
hex_DTH = ''
denaryDTH = 0
def denarytohex():
    global hex_DTH
    global denaryDTH
    #denaryDTH = int(input(""))
    hex_DTH = ''
    bs = ''
    while denaryDTH !=0:
        r = denaryDTH%16 #remainder
        if int(r) ==10:
            bs = bs + 'A'
        elif int(r) == 11:
            bs = bs + 'B'
        elif int(r) == 12:
            bs = bs + 'C'
        elif int(r) == 13:
            bs = bs + 'D'
        elif int(r) == 14:
            bs = bs + 'E'
        elif int(r) == 15:
            bs = bs + 'F'
        else:
            bs = bs+str(r)
        denaryDTH= denaryDTH // 16
    print("\nThe hexadecimal number is:",bs[::-1])
    return

#HEX TO DENARY
denaryNum = 0
def hextodenary():
  
  hexiNumber = input("Input the Hexidecimal number:  ")
  numHex = len(hexiNumber)
  global denaryNum

  for bit in range(0, numHex):
    if hexiNumber[bit] == 'A':
      hexBit = 10
    elif hexiNumber[bit] == 'B':
      hexBit = 11
    elif hexiNumber[bit] == 'C':
      hexBit = 12
    elif hexiNumber[bit] == 'D':
      hexBit = 13
    elif hexiNumber[bit] == 'E':
      hexBit = 14
    elif hexiNumber[bit] == 'F':
      hexBit = 15
    else:
      hexBit = int(hexiNumber[bit])
    denaryNum = denaryNum + (int(hexBit) * 16**(numHex - 1 - bit))

  print("Your Hexidecimal number converted into denary is \n", denaryNum)
  return
print("----------------------------------")
print("Welcome to the AMAZING Calculator! - By ADV08 ")
print("----------------------------------")
print("What operation would you like to take place? \n")
print("For binary, please enter [B], For HEXADECIMAL please ente[H], for Denary, please ENTER [D] : ")

operation = input("")

if operation == 'B':
    binaryNUMBER = input("Enter binary number : ")
    binarytodenary(binaryNUMBER)
    denaryDTH = DENARYNUM
    denarytohex()

    
if operation == 'D':
    denaryDTB = int(input("Enter denary number : "))
    denaryDTH = denaryDTB 

    denarytobinary()
    denarytohex()
if operation == 'H':
    hextodenary()
    denaryDTB = denaryNum
    denarytobinary()
   
    

    

