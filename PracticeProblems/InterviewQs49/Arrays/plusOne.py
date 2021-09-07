#each member of an array makes up a large integer, add 1 to that integer
def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)-1
        summ = 0
        for i, val in enumerate(digits):
            summ += 10**(l - i)*val #multiply out using powers of 10
        summ += 1 #add 1
        return [int(j) for j in str(summ)] #break up number into individual digits

#testing
test = [9]
print(plusOne(test))