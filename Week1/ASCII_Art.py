# program for ASCII art Encoding
# Sabelo Dlamini
# 12 March 2024

def encodeString(stringVal):
    myList = []
    currChar = stringVal[0]
    counter=0
    
    for x in range(len(stringVal)):
        if stringVal[x] == currChar:
            counter += 1
        else:
            myList.append((currChar,counter))
            currChar = stringVal[x]
            counter=1
              
    myList.append((currChar,counter))  
    return myList


def decodeString(encodedList):
    decodeStringvar = ''
    for i in encodedList:
        decodeStringvar = decodeStringvar + i[0]*i[1]
        
    return decodeStringvar



print(encodeString('AAAAABBBBAAA'))
dlist = [('A',5),('B',4),('A',3)]
print(decodeString(dlist))