import random
NAV = ["LEFT","FRONT","RIGHT","BACK"]
NUM = random.randint(1,3)
NAVG = ""
for C in range(NUM,1,-1):
 NAVG = NAVG + NAV[C]
print(NAVG)