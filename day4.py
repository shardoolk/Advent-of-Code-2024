#### Day4: Ceres Search ---

grid = open("input_day4.txt").readlines()

#### Part 1: Counting occurence of the string "XMASS" in the grid horizontally, vertically and diagonally

### Convert array to numpy array to make it more intuitive
import numpy as np
grid = [list(line.strip()) for line in grid]
grid = np.array(grid)

nrows, ncols = grid.shape

n_horizontal = 0
# Check horizontal
for row in grid:
    for i in range(ncols - 3):
        if np.array_equal(row[i:i+4], ['X', 'M', 'A', 'S']):
            n_horizontal += 1
        elif np.array_equal(row[i:i+4], ['S', 'A', 'M', 'X']):
            n_horizontal += 1 

# Check vertical         
transposed_grid = grid.T
n_vertical = 0
for row in transposed_grid:
    for i in range(ncols - 3):
        if np.array_equal(row[i:i+4], ['X', 'M', 'A', 'S']):
            n_vertical += 1
        elif np.array_equal(row[i:i+4], ['S', 'A', 'M', 'X']):
            n_vertical += 1



print(n_horizontal)
print(n_vertical)            

# Check diagonal
n_diagonal = 0

for i in range(nrows - 3):
    for j in range(ncols - 3):
        if np.array_equal([grid[i, j], grid[i+1, j+1], grid[i+2, j+2], grid[i+3, j+3]], ['X', 'M', 'A', 'S']):
            n_diagonal += 1
        elif np.array_equal([grid[i, j], grid[i+1, j+1], grid[i+2, j+2], grid[i+3, j+3]], ['S', 'A', 'M', 'X']):
            n_diagonal += 1 
            
for i in range(nrows - 3):
    for j in range(ncols - 3):
        if np.array_equal([grid[i, j+3], grid[i+1, j+2], grid[i+2, j+1], grid[i+3, j]], ['X', 'M', 'A', 'S']):
            n_diagonal += 1
        elif np.array_equal([grid[i, j+3], grid[i+1, j+2], grid[i+2, j+1], grid[i+3, j]], ['S', 'A', 'M', 'X']):
            n_diagonal += 1
            
print(n_diagonal)            

print("Part 1 : ", n_horizontal + n_vertical + n_diagonal)


#### Part 2: Counting Xmasses shape
def counting_Xmasses(grid):
    Part2 = 0
    for i in range(1,nrows-1):
        for j in range(1, ncols-1):
            if grid[i, j] == 'A' and grid[i+1,j+1] =='S' and grid[i+1, j-1] == 'S' and grid[i-1,j+1] == 'M' and grid[i-1,j-1] == 'M':
                Part2 += 1
            elif grid[i,j] =='A' and grid[i+1,j-1] =='M' and grid[i+1,j+1] =='M' and grid[i-1,j-1] =='S' and grid[i-1,j+1] =='S':
                Part2 += 1
    return Part2
            
            
normal_gridXs = counting_Xmasses(grid)
transposed_gridXs = counting_Xmasses(transposed_grid)


print("Part 2 : ", normal_gridXs + transposed_gridXs)        