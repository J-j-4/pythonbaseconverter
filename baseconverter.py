base1 = int(raw_input("What base are you working in:"))
n_to_change = int(str(raw_input("Number to change:")),base1)
base2 = int(raw_input("What base do you want to convert to:"))

def baseto10(number,base):
    total = 0
    num = str(number)
    num = num[::-1]
    for n in range(0,len(num)):
        digit = num[n]
        total = total + (int(digit) * int(base) ** int(n))
    return total

base10 = baseto10(n_to_change,base1)
    
def digitcon(digit,n6):
        if digit < 10:
            return chr(ord('0') + digit)
        else:
            return chr(ord('a') + digit - 10).upper()
   

def baseconverter(number,n5):
    (d,m) = divmod(number,n5)
    if d:
        return baseconverter(d,base10) + digitcon(m,n5)
    else:
        return digitcon(m,n5)

print "The new number is:",baseconverter(base10,base2)



