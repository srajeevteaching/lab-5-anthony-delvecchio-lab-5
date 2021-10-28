# Programmers: Anthony DelVecchio
# Course: CS151, Dr. Rajeev
# Date: 10/21/21
# Lab Number: 5
# Program Inputs: Type of floor for the 5 rooms and dimensions
# Program Outputs: Total cost and cost per square foot

# Define Function for Cost per Square Foot
def cost(floor):
    if floor == "hardwood":
        cost = 1.39
    elif floor == "carpet":
        cost = 3.99
    elif floor == "tile":
        cost = 4.99
    else:
        cost = 0
    print("The cost per square foot of this floor is:", cost)
    return cost
# Define Function for Total Cost
def totalcost(l, w, floor):
    area = l * w
    if floor == "hardwood":
        totalcost = 1.39 * area
    elif floor == "carpet":
        totalcost = 3.99 * area
    elif floor == "tile":
        totalcost = 4.99 * area
    else:
        totalcost = 0
    print("The total cost of this floor is:", totalcost)
    return totalcost
# Define Main function
def main():
    floor = input("What type of floor would you like? ")
    floor = floor.strip().lower()
    lengthRaw = input("Input Length: ")
    widthRaw = input("Input Width: ")
    l = int(lengthRaw)
    w = int(widthRaw)
    cost(floor)
    totalcost(l, w, floor)
# Run Functions 1 time for each floor
main()
main()
main()
main()
main()