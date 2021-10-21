# Programmers: Anthony DelVecchio
# Course: CS151, Dr. Rajeev
# Date: 10/21/21
# Lab Number: 5
# Program Inputs: Type of floor for the 5 rooms and dimensions
# Program Outputs: Total cost and cost per square foot

# Define Functions for Each Floor
def totalcost1():
    l = input(float("Input Length: "))
    w = input(float("Input Width: "))
    area = l * w
    if floor1 == "hardwood":
        totalcost = 1.39 * area
    elif floor1 == "carpet":
        totalcost = 3.99 * area
    elif floor1 == "tile":
        totalcost = 4.99 * area
    else:
        totalcost = 0
    return totalcost
def totalcost2():
    l = input(float("Input Length: "))
    w = input(float("Input Width: "))
    area = l * w
    if floor2 == "hardwood":
        totalcost = 1.39 * area
    elif floor2 == "carpet":
        totalcost = 3.99 * area
    elif floor2 == "tile":
        totalcost = 4.99 * area
    else:
        totalcost = 0
    return totalcost
def totalcost3():
    l = input(float("Input Length: "))
    w = input(float("Input Width: "))
    area = l * w
    if floor3 == "hardwood":
        totalcost = 1.39 * area
    elif floor3 == "carpet":
        fotalcost = 3.99 * area
    elif floor3 == "tile":
        totalcost = 4.99 * area
    else:
        totalcost = 0
    return totalcost
def totalcost4():
    l = input(float("Input Length: "))
    w = input(float("Input Width: "))
    area = l * w
    if floor4 == "hardwood":
        totalcost = 1.39 * area
    if floor4 == "carpet":
        totalcost = 3.99 * area
    if floor4 == "tile":
        totalcost = 4.99 * area
    else:
        totalcost = 0
    return totalcost
def totalcost5():
    l = input(float("Input Length: "))
    w = input(float("Input Width: "))
    area = l * w
    if floor5 == "hardwood":
        totalcost = 1.39 * area
    if floor5 == "carpet":
        totalcost = 3.99 * area
    if floor5 == "tile":
        totalcost = 4.99 * area
    else:
        totalcost = 0
    return totalcost
# User Inputs
floor1 = input(str("Choose between hardwood, carpet, or tile: "))
floor1 = floor1.strip().lower()
totalcost1()
floor2 = input(str("Choose between hardwood, carpet, or tile: "))
floor2 = floor2.strip().lower()
totalcost2()
floor3 = input(str("Chose between hardwood, carpet, or tile: "))
floor3 = floor3.strip().lower()
totalcost3()
floor4 = input(str("Choose between hardwood, carpet, or tile: "))
floor4 = floor4.strip().lower()
totalcost4()
floor5 = input(str("Choose between hardwood, carpet, or tile: "))
floor5 = floor5.strip().lower()
totalcost5()
cost1 = 0
cost2 = 0
cost3 = 0
cost4 = 0
cost5 = 0
if floor1 == "hardwood":
    cost1 = 1.39
elif floor1 == "carpet":
    cost1 = 3.99
elif floor1 == "tile":
    cost1 = 4.99
elif floor1 != "hardwood" and floor1 != "carpet" and floor1 != "tile":
    cost1 = 0
if floor2 == "hardwood":
    cost2 = 1.39
elif floor2 == "carpet":
    cost2 = 3.99
elif floor2 == "tile":
    cost2 = 4.99
elif floor2 != "hardwood" and floor2 != "carpet" and floor2 != "tile":
    cost2 = 0
if floor3 == "hardwood":
    cost3 = 1.39
elif floor3 == "carpet":
    cost3 = 3.99
elif floor3 == "tile":
    cost3 = 4.99
elif floor3 != "hardwood" and floor2 != "carpet" and floor2 != "tile":
    cost3 = 0
if floor4 == "hardwood":
    cost4 = 1.39
elif floor4 == "carpet":
    cost4 = 3.99
elif floor4 == "tile":
    cost4 = 4.99
elif floor4 != "hardwood" and floor2 != "carpet" and floor2 != "tile":
    cost4= 0
if floor5 == "hardwood":
    cost5 = 1.39
elif floor5 == "carpet":
    cost5 = 3.99
elif floor5 == "tile":
    cost5 = 4.99
elif floor5 != "hardwood" and floor2 != "carpet" and floor2 != "tile":
    cost5 = 0
print("The cost per square foot of Floor 1 is: ", cost1)
