''' This file is used to create all the initial matrixes for temperature distribution across
    the entire grid at t = 0'''

import numpy as np
import matplotlib.pyplot as plt

infi = 999999999999.0

sizeX = 10.0
sizeY = 10.0
deltaTheta = 0.2       # Dimensionless time steps

countX = int(sizeX)
countY = int(sizeY)
count_checker = (countX-2)*(countY-2)
tempA = np.zeros(shape=(sizeX,sizeY))
tempB = np.zeros(shape=(sizeX,sizeY))
tempC = np.zeros(shape=(sizeX,sizeY))
tempW1 = np.zeros(shape=(sizeX,sizeY))
tempW2 = np.zeros(shape=(sizeX,sizeY))

# Constants

Na = 0.5
deltaX = Na/sizeX
deltaY = Na/sizeY

timesteps = 50

# For fluid B
Vb = 0.0
phi = 0.5     # Unsure of this value
Peb = infi

# For Wall 1
Si = 0.5
Rab = 1.0
lamdaX = 0.0
lamdaY = 0.0

# For Wall 2
Rcb = 1.0

# For Fluid A
Va = 0.0
Eab = 0.5
Pea = infi

# For Fluid C
Vc = 0.0
Ecb = 0.5
Pec = infi

# Getting initial input over fluid B

for j in range(countY):
  tempB[0,j] = 1.0         # For constant input

for j in range(countY):
  tempC[0,j] = 1.0         # For constant input
