#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I
# Give an analysis of the running time of each snippet of pseudocode with respect to the input size n

a)
O(1)

b)
O(n)


c)
O{N^2}

## Exercise II

The egg will break depending on which side of floor f it is (higher or lower).

Algorithm will take in two attributes: how tall the building, and the floor that the egg will break.

The algorithm should sort the floors by level: ground floor (0), floor 1, floor 2...

Then find floor f in the array of floor levels and set it as the breaking point. This requires searching through the list. The quickets way would be to

Run time complex: O(n)

break_egg(floors, break_point):
    for floor in floors:
        if floor < break_point:
            return True
        if floor > break_point: 
            return False

