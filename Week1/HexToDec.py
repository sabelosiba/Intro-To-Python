# program to convert hexaDecimal to Decimal
# Sabelo Dlamini
# 12 March 2024

hexNumbers = {'0':0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'A': 10,'B': 11,'C': 12,'D': 13,'E': 14,'F': 15}


def hexToDec(hexNum):
    decimal = 0
    for c in hexNum:
        if c not in hexNumbers:
            return None
    
    hexLen = len(hexNum) 
    i=0
    while (hexLen > 0 ):
        decimal = decimal + ( hexNumbers[hexNum[i]] * 16**(hexLen-1) )
        i = i + 1
        hexLen = hexLen-1
    return decimal


print(hexToDec('AA'))