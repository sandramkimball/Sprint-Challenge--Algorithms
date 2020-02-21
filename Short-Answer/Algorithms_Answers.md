#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I
# Give an analysis of the running time of each snippet of pseudocode with respect to the input size n

a) 
    O(1) - one action happening, one level of basic math. Fast.

b)
    O(n log n) - a for loop + while loop, which condences into a single n action. Medium speed range, but still good. 


c)
    O(n^2) - recursive. It's a simple action O(n), just being ran over and over. Slow. But can be improved using cache to an extent.

## Exercise II

The egg will break depending on which side of floor f it is (higher or lower).

Algorithm will take in two attributes: how tall the building, and the floor that the egg will break.

The algorithm should sort the floors by level: ground floor (0), floor 1, floor 2...

Then find floor f in the array of floor levels and set it as the breaking point. This requires searching through the list. The quickets way would be to

Run time complex: binary search will be a hair faster, but I feel this would be a small enough scope to use linear search as well. 0(n)

break_egg(floors, break_point):
    for floor in floors:
        if floor < break_point:
            return True
        if floor > break_point: 
            return False

