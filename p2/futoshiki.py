import os
import sys
from constraint import *

path = sys.argv[1]

file_path = os.path.abspath(path)

f = open(file_path, "r")


futoshiki_array = []
for file in f:
    for i in file.strip().split(", "):
        futoshiki_array.append(i)


#####constraint################

f.close()

problem = Problem()


problem.addVariables(["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4", "D1", "D2", "D3", "D4"],[1, 2, 3, 4])

problem.addConstraint(AllDifferentConstraint(), ["A1", "A2", "A3", "A4"])
problem.addConstraint(AllDifferentConstraint(), ["B1", "B2", "B3", "B4"])
problem.addConstraint(AllDifferentConstraint(), ["C1", "C2", "C3", "C4"])
problem.addConstraint(AllDifferentConstraint(), ["D1", "D2", "D3", "D4"])
problem.addConstraint(AllDifferentConstraint(), ["A1", "B1", "C1", "D1"])
problem.addConstraint(AllDifferentConstraint(), ["A2", "B2", "C2", "D2"])
problem.addConstraint(AllDifferentConstraint(), ["A3", "B3", "C3", "D3"])
problem.addConstraint(AllDifferentConstraint(), ["A4", "B4", "C4", "D4"])



a = 0
b = 1

for i in futoshiki_array:
    #####check array lenght##########
    if (a > len(futoshiki_array) or b > len(futoshiki_array)):
        break

    first = futoshiki_array[a]
    second = futoshiki_array[b]

    ##########check numeric##############
    if second.isnumeric():
        second = int(second)
        problem.addConstraint(ExactSumConstraint(second), [first])


    else:

        problem.addConstraint(lambda first, second: first > second, (first, second))

    b = b + 2
    a = a + 2


comma = ", "

result = problem.getSolutions()[0]

output = str(result["A1"]) + comma +  str(result["A2"]) + comma + str(result["A3"]) + comma + str(result["A4"]) + "\n" +\
         str(result["B1"]) + comma +  str(result["B2"]) + comma + str(result["B3"]) + comma + str(result["B4"]) + "\n" + \
         str(result["C1"]) + comma +  str(result["C2"]) + comma + str(result["C3"]) + comma + str(result["C4"]) + "\n" +\
         str(result["D1"]) + comma +  str(result["D2"]) + comma + str(result["D3"]) + comma + str(result["D4"])



futoshiki_output = open("futoshiki_output.txt", "w")
futoshiki_output.write(output)


futoshiki_output.close()




