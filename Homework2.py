# -*- coding: utf-8 -*-
"""
@author: Diego Pérez Reyes
"""

import numpy as np

"""
Convertidor coordenadas cartesianas a polares
"""
def convert_car(x,y):
    r = np.sqrt(x ** 2 + y ** 2)
    
    if x != 0:
        theta = np.arctan(y/x)
    else:
        theta = np.pi / 2
        if y < 0:
            theta *= 3
    
    return round(r,2), round(theta,2)

#Ejemplo
#print(convert_car(0, 1))

"""
Convertidor coordenadas polares a cartesianas
"""
def convert_pol(r,theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    return round(x,2), round(y,2)

#Ejemplo
#print(convert_pol(2, (11 * np.pi) / 6))
