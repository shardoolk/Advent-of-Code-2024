### Day 2 : --- Day 2: Red-Nosed Reports ---

data = open("input_day2.txt").read().strip().split('\n')


safe = 0

### use of set function in matlab to check if the difference between the numbers is 1, 2 or 3
for line in data:
    line_arr = []
    line_arr = [int(y) for y in line.split(' ')]
    inc = [line_arr[i+1] - line_arr[i] for i in range(len(line_arr)-1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        safe = safe + 1


print("Part 1 : ",safe)

### Part 2

## modify the row by removing one element and check if the difference between the numbers is 1, 2 or 3 use set again
safe_count_part2 = 0
data = open("input_day2.txt").read().strip().split('\n')
data = [[int(y) for y in line.split(' ')] for line in data]
for line in data:
    for i in range(len(line)):
        modified_row = line[:i] + line[i + 1:]
        differences = [modified_row[j + 1] - modified_row[j] for j in range(len(modified_row) - 1)]
        if set(differences) <= {1, 2, 3} or set(differences) <= {-1, -2, -3}:
            safe_count_part2 += 1
            break  # Stop checking further for this row since it's already valid

print("Part 2 : ",safe_count_part2)