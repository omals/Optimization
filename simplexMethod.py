import numpy as np

np.set_printoptions(suppress=True)
maxORmin = 1 #for maximisation 1,minimization 0

cObjectiveFn = np.array([6.0,8.0,0.0,0.0])

cConstraintEqn = np.array([[5.0,10.0,1.0,0.0],[4.0,4.0,0.0,1.0]])

solution = np.array([[60.0],[40.0]])

cSlack = np.array([[0.0],[0.0]])

# solutionTranspose = np.transpose(solution)

simplexTable = np.hstack((cConstraintEqn, solution))


print("\nSimplex Method Table : \n")
print(simplexTable)

zj = []

for i in range(4):
    tempProduct = np.multiply(simplexTable[:,i], cSlack)
    zj.append(np.sum(tempProduct))

print("\nInitial values of Zj   : ",zj)


Zj = np.array(zj)
# print("")


CjZjDiff = cObjectiveFn - Zj

print("Cj - Zj                : ",CjZjDiff)


# print("")

selectedColumn = list(CjZjDiff).index(max(CjZjDiff))

#selectedColumn= selectedColumn
print("Selected Column        : ",selectedColumn+1)

print("Selected column values : ",simplexTable[:,selectedColumn])
# print(simplexTable[:,selectedColumn])

ratio = []

for i in range(2):
    ratio.append(solution[i][0]/simplexTable[i][selectedColumn])

print("Ratio                  : ",ratio)

selectedRow = list(ratio).index(min(ratio))

print("Selected Row           : ",selectedRow+1)

print("Key value              : ",simplexTable[selectedRow][selectedColumn])

#print(simplexTable[selectedRow][selectedColumn])

print("")


simplexTable[selectedRow,:] = simplexTable[selectedRow,:]/simplexTable[selectedRow][selectedColumn]

# simplexTable[selectedRow,:] =  np.divide(simplexTable[selectedRow,:],simplexTable[selectedRow][selectedColumn])

#print("\nUpdated Simplex Table : ")
#print(simplexTable)

print("")

cSlack[selectedRow] = cObjectiveFn[selectedColumn]

print("CBi : ")
print(cSlack)



#print("\nUpdated Simplex Table : ")
#print(simplexTable)

simplexTable[selectedRow+1, :] = simplexTable[selectedRow+1, :] - (simplexTable[selectedRow+1][selectedColumn]*simplexTable[selectedRow,:])

print("\nUpdated Table : ")
print(simplexTable)

print("")

Zj2 = []


for i in range(4):
    tempProduct = np.multiply(cSlack.transpose(),simplexTable[:,i])
    Zj2.append(np.sum(tempProduct))

print("\nZj2 values             : ",Zj2)

CjZjDiff = cObjectiveFn - Zj2

print("Cj - Zj                : ",CjZjDiff)

# print("")

selectedColumn = list(CjZjDiff).index(max(CjZjDiff))

print("Selected Column        : ",selectedColumn+1)

print("Selected column values : ",simplexTable[:,selectedColumn])
# print(simplexTable[:,selectedColumn])

ratio2 = []

for i in range(2):
    ratio2.append(solution[i][0]/simplexTable[i][selectedColumn])

print("Ratio                  : ",ratio2)

selectedRow = list(ratio2).index(min(ratio2))

print("Selected Row           : ",selectedRow+1)

print("Key value              : ",simplexTable[selectedRow][selectedColumn])

simplexTable[selectedRow,:] = simplexTable[selectedRow,:]/simplexTable[selectedRow][selectedColumn]

print("")

cSlack[selectedRow] = cObjectiveFn[selectedColumn]

print("CBi : ")
print(cSlack)

simplexTable[selectedRow-1, :] = simplexTable[selectedRow-1, :] - (simplexTable[selectedRow-1][selectedColumn]*simplexTable[selectedRow,:])

print("\nUpdated Simplex Table : ")
print(simplexTable)

print("")

Zj3 = []


for i in range(4):
    tempProduct = np.multiply(cSlack.transpose(),simplexTable[:,i])
    Zj3.append(np.sum(tempProduct))

print("Zj2 values           : ",Zj3)

CjZjDiff = cObjectiveFn - Zj3

print("Cj - Zj              : ",CjZjDiff)
print("")
print("\nSolution : ")
print("X : ",simplexTable[1][4],"  Y : ",simplexTable[0][4])
zOptimum = []

zOptimum.append(np.sum(np.multiply(cSlack.transpose(),simplexTable[:,4])))
print("Z( Optimum ) : ",zOptimum)
print("")