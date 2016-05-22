# Base Converter Program - Converts from any desired base to any base ranging 
# from 2-64.

"""
Below are the three main variables for the code, the number to change, 
the original base the number you are converting is in, and the base you would 
like to convert to.
"""

n_to_change = raw_input("Number to change:")
base1 = int(raw_input("Original base:"))
base2 = int(raw_input("Base you are changing to:"))

"""
This is a function that converts integers into base 10 
from any base provided, over decimal bases, such as hexadecimal bases. 
"""
err = 0
def to10fromlarge(n,b):    
    numbasehex = {"1": 1, "0": 0, "2": 2, "3": 3, "4": 4, 
    "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, 'B': 11, 
    'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 
    'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 
    'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 
    'X': 33, 'Y': 34, 'Z': 35}
    n1 = str(n)
    new = 0
    power = 0
    ver = str(n[::-1])
    
    # Checks if number is valid in the given base, prints ERROR, if not.
    
    for i in ver:
        if numbasehex[i] < base1:
            new = new + numbasehex[i] * (int(b) ** power)
            power = power + 1
            test = 0
        else:
            print ""
            print i + " is not a valid number in base " + str(base1) + "."
            print ""
            new = "ERROR"
            break
    return new
    
"""    
Below is a function that converts the new base 10 number into the arbitrary 
base chosen by the user.
"""

def base10toN(num,n):
    #Change a  to a base-n number.
    #Up to base-36 is supported without special notation.
    num_rep={10:'A', 11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:
    'I',19:'J',20:'K',21:'L',22:'M',23:'N',24:'O',25:'P',26:'Q',27:'R',
    28:'S',29:'T',30:'U',31:'V',32:'W',33:'X',34:'Y', 35:'Z'}
    # Below is how the computer converts through the numbers.    
    new_num_string=''
    current=num
    
    """
     Using a while loop to finder remainders and calculate the correct numbers. 
    Seeing if the base is less than 36, than going through the correct steps.
    """
    if current == "ERROR":
        print "An ERROR has occurred, you have likely input a number too large for that base!"
        print ""
    else:
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
                
            # Prints the number you are changing, the base it was originally in. Then the number in the new base, with the base.
        return n_to_change + "(Base:" + str(base1) + ")" + " is " + new_num_string + " in base " + str(base2) + "."
"""    
This checks if the base the original number is in is equal to ten, 
to make calculations easier. Otherwise, runs to10fromlarge, and etc.
"""


print base10toN(to10fromlarge(n_to_change,base1),base2)




