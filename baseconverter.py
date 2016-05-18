# Base Converter Program - Converts from any desired base to any base ranging from 2-64
# Developed by Nora Rooney, Robert Brodin, and Robert Mennino

# Below are the three main variables for the code, the number to change, the original base the number you are converting is in, and the base you would like to convert to.

n_to_change = raw_input("Number to change:")
base1 = int(raw_input("Original base:"))
base2 = int(raw_input("Base you are changing to:"))

# Below is a function to convert integers into base ten, we have two seperate functions for numbers under 10 and over 10.

def baseto10(number,base):
    total = 0
    num = str(number)
    num = num[::-1]
    for n in range(0,len(num)):
        digit = num[n]
        total = total + (int(digit) * int(base) ** int(n))
    return total

def to10fromlarge(n,b):    
    numbasehex = {"1": 1, "0": 0, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    n1 = str(n)
    new = 0
    power = 0
    ver = str(n[::-1])
    for i in ver:
        new = new + numbasehex[i] * (int(b) ** power)
        power = power + 1
    return new
        
def base10toN(num,n):
    #Change a  to a base-n number.
    #Up to base-36 is supported without special notation.
    num_rep={10:'a',
         11:'b',
         12:'c',
         13:'d',
         14:'e',
         15:'f',
         16:'g',
         17:'h',
         18:'i',
         19:'j',
         20:'k',
         21:'l',
         22:'m',
         23:'n',
         24:'o',
         25:'p',
         26:'q',
         27:'r',
         28:'s',
         29:'t',
         30:'u',
         31:'v',
         32:'w',
         33:'x',
         34:'y',
         35:'z'}
    new_num_string=''
    current=num
    while current!=0:
        remainder=current%n
        if 36>remainder>9:
            remainder_string=num_rep[remainder]
        elif remainder>=36:
            remainder_string='('+str(remainder)+')'
        else:
            remainder_string=str(remainder)
        new_num_string=remainder_string+new_num_string
        current=current/n
    return n_to_change + " - (Base:" + str(base1) + ")" + " is " + new_num_string + " in base " + str(base2) + "."
    
if base1 < 10:
    print base10toN(baseto10(int(n_to_change),base1),base2)
elif base1 == 10:
    print base10toN(int(n_to_change),base2)
elif base1 > 10:
    print base10toN(to10fromlarge(n_to_change,base1),base2)
    

