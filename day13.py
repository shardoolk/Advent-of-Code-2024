######--- Day 13: Claw Contraption ---

commands = open("test_day13.txt").read().strip().split("\n\n")

import re
import numpy as np
tol = 1e-6

tokens = 0
for command in commands:
    buttonA, buttonB, prize = command.split("\n")
    buttonA = buttonA.split(":")[-1].strip()
    buttonB = buttonB.split(":")[-1].strip()
    xA, yA = map(int, re.findall(r"\d+", buttonA))
    xB, yB = map(int, re.findall(r"\d+", buttonB))
    pA, pB = map(int, re.findall(r"\d+", prize))
    
    ### Adding 10000000000000 for part 2
    #pA = 10000000000000+ pA 
    #pB = 10000000000000 + pB
    
    A = np.array([[xA, xB], [yA, yB]])
    B = np.array([pA, pB])
    C = np.linalg.solve(A, B)
    
    ### Was causing a bug in the code Maybe an elegant way to check if the values are integers is possible    
    are_integers = np.all(np.isclose(C, np.round(C), atol=tol))
    
    if are_integers:
        ### Remove this check for part 2
        if C[0] <= 100 and C[1] <= 100:
            tokens += 3*C[0] + C[1]
        
print("Part 1: ", tokens)        


