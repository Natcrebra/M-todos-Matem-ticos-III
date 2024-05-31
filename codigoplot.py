#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:53:47 2024

@author: nat
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir funciones x(t) y y(t)
def x(t):
    return 21 * np.cos(t) + 11.5 * np.cos(3*t) + 11.5 * np.cos(9*t)

def y(t):
    return 21 * np.sin(t) - 11.5 * np.sin(3*t) - 11.5 * np.sin(9*t)

# Generar valores de t
t_values = np.linspace(0, 2*np.pi, 1000)

# Calcular los valores de x(t) e y(t)
x_values = x(t_values)
y_values = y(t_values)

# Trazar las funciones x(t) e y(t)
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='Trayectoria')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trayectoria paramétrica en el plano xy')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()