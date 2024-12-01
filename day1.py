### --- Day 1: Historian Hysteria ---


from collections import Counter
data = open("input_day1.txt").read().strip().split('\n')

leftCol = [] 
rightCol = []
for line in data:
    left,right = line.split('  ')
    leftCol.append(left)
    rightCol.append(right) 
    

## sort the columns    
rightCol.sort()
leftCol.sort()

## Part 1 : Difference between the columns

print("Part 1 : ",sum(abs(int(leftCol[i]) - int(rightCol[i])) for i in range(len(leftCol))))



## Paert 2 : Count the number of times a number in the left column appears in the right column and multiply it by the number in the left column
## Uses counter for faster exection
rightCol_counts = Counter(map(int, rightCol)) 
result = sum(int(leftCol[i]) * rightCol_counts[int(leftCol[i])] for i in range(len(leftCol)))

print("Part 2 : ",result)