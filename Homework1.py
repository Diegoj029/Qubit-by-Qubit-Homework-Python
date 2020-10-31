# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 00:03:21 2020

@author: diego
"""

""""
Question 1
Convert the following binary numbers to base 10
"""
def convert_base2(num):
    base2 = [int(x) for x in str(num)]
    base10 = 0
    power = len(base2)-1
        
    for digit in base2:
        base10 += digit * (2 ** power)
        power -= 1
        
    return base10

#Ejemplo:
#print(convert_base2(11010111))


""" 
Question 2
Convert the following base 10 numbers to binary
"""
def convert_base10(num):
    base2 = ''
    
    while num > 0:
        if num % 2 > 0:
            base2 = '1' + base2
        else:
            base2 = '0' + base2
        num = num // 2

    return base2

#Ejemplo:
#print(convert_base10(146))


"""
Question 3
Add the following binary numbers
"""
def sum_binary(num1, num2):
    n1 = [int(x) for x in str(num1)]
    n2 = [int(x) for x in str(num2)]
    res = []
    residuo = 0
    
    if len(n1) > len(n2):
        for i in range(len(n1)-len(n2)):
            n2.insert(0,0)
    else:
        for i in range(len(n2)-len(n1)):
            n1.insert(0,0)
            
    n1.reverse()
    n2.reverse()
    
    for i in range(len(n2)):
        suma = n1[i] + n2[i] + residuo
        if suma > 1:
            res.append(suma - 2)
            residuo = 1
        else:
            res.append(suma)
            residuo = 0
    
    if residuo > 0:
        res.append(1)
            
    res.reverse()
    
    return res

#Ejemplo:
print(sum_binary(1101, 1011))