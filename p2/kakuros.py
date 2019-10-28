import sys
import os
from constraint import *

path = sys.argv[1]

file_path = os.path.abspath(path)

file = open(file_path, "r")

tmp = []
for file in file:
    for i in file.strip().split(", "):
        tmp.append(i)
len = int((len(tmp)))
middle = int(len /2)
kakuro_array = []

kakuro_array.append(tmp[0:middle])
kakuro_array.append(tmp[-middle:])

#print(kakuro_array)

##Problem Solve

problem = Problem()

problem.addVariables(["x1","x2","x3","y1","y2","y3","z1","z2","z3"],[1,2,3,4,5,6,7,8,9])


column1 = int(kakuro_array[0][0])
column2 = int(kakuro_array[0][1])
column3 = int(kakuro_array[0][2])
row1 = int(kakuro_array[1][0])
row2 = int(kakuro_array[1][1])
row3 = int(kakuro_array[1][2])


problem.addConstraint(AllDifferentConstraint(), ["x1", "x2", "x3"])
problem.addConstraint(AllDifferentConstraint(), ["y1", "y2", "y3"])
problem.addConstraint(AllDifferentConstraint(), ["z1", "z2", "z3"])
problem.addConstraint(AllDifferentConstraint(), ["x1", "y1", "z1"])
problem.addConstraint(AllDifferentConstraint(), ["x2", "y2", "z2"])
problem.addConstraint(AllDifferentConstraint(), ["x3", "y3", "z3"])
problem.addConstraint(ExactSumConstraint(row1), ["x1", "x2", "x3"])
problem.addConstraint(ExactSumConstraint(row2), ["y1", "y2", "y3"])
problem.addConstraint(ExactSumConstraint(row3), ["z1", "z2", "z3"])
problem.addConstraint(ExactSumConstraint(column1), ["x1", "y1", "z1"])
problem.addConstraint(ExactSumConstraint(column2), ["x2", "y2", "z2"])
problem.addConstraint(ExactSumConstraint(column3), ["x3", "y3", "z3"])



solutionSet = problem.getSolutions()[0]
comma = ", "

x1 = str(solutionSet["x1"])
x2 = str(solutionSet["x2"])
x3 = str(solutionSet["x3"])
y1 = str(solutionSet["y1"])
y2 = str(solutionSet["y2"])
y3 = str(solutionSet["y3"])
z1 = str(solutionSet["z1"])
z2 = str(solutionSet["z2"])
z3 = str(solutionSet["z3"])

output = "x" + comma + str(column1) +comma +str(column2) +comma +str(column3) + "\n"\
         + str(row1) + comma +x1 + comma + x2 +comma +x3 +"\n" \
         + str(row2) +comma +y1 +comma +y2 + comma +y3 + "\n"\
         + str(row3) +comma +z1 +comma +z2 + comma +z3


kakuro_output = open("kakuro_output.txt", "w")
kakuro_output.write(output)















