
def reverse(x):
    if x<0:
        x*=-1
        neg = True
    digits = [int(d) for d in str(x)]
    digits.reverse()
    if x == 0:
        return 0
    for i in range(len(digits)):
        if digits[i] == 0:
            digits.remove(digits[i])
        else:
            break
    strings = [str(integer) for integer in digits]
    intString = "".join(strings)
    integer = int(intString)
    if(neg):
        integer*=-1
    return integer
    

print(reverse(-33))