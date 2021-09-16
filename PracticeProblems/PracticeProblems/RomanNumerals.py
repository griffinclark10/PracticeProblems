def romanToInt(s):
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        summ = 0
        integers = []
        for i in s:
            integers.append(roman[i])
        for i in range(len(integers)-1):
            if integers[i] < integers[i+1]:
                integers[i]*=-1
            summ += integers[i]
        summ += integers[len(integers)-1]
        return summ

            
print(romanToInt("MCMXCIV"))
        
        