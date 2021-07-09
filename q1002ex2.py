#def main ( ) :
Moves=[11, 22, 33, 44]
Queen=Moves
Moves[2]+=22
L=len(Moves)
for i in range (L):
  print ("Now@", Queen[L-i-1],"#", Moves [i])