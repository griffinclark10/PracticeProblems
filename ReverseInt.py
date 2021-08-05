
def reverse(x):
    neg = False
    if x == 0: return 0
    if x<0:
        x*=-1
        neg = True
    digits = [int(d) for d in str(x)] #make the integer into a slist of strings
    digits.reverse() #reverse the list
    strings = [str(integer) for integer in digits]
    intString = "".join(strings) #join the strings 
    integer = int(intString) #make the string an integer
    if(neg):
        integer*=-1 
    if integer > -0x80000000 and integer< 0x7fffffff: #make sure the return value is a 32 bit integer
        return integer
    else: 
        return 0
    

print(reverse(900000))