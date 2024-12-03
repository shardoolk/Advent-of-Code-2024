####--- Day 3: Mull It Over ---

data = open('input_day3.txt').read().strip()

#### Regex patterns verified from stackoverflow and reddit posts
import re
def values_from_match(matches):
    total = 0
    for match in matches:
        match = match[4:-1]
        a, b = map(int, match.split(','))
        total += a * b
    return total
    
    

# Define the pattern for 'mul()' string in the data string
pattern = r"mul\(\d+,\d+\)"

matches = re.findall(pattern, data)

print("Part 1: ", values_from_match(matches))



##### Define a pattern to remove the string between the don't() and do() strings
pattern2 = r"don't\(\).*?(?:$|do\(\))"

## data2 is the data with the string between don't() and do() removed
data2 = re.sub(pattern2, '', data, flags=re.DOTALL)
matches2 = re.findall(pattern, data2)
part2 = 0

print("Part 2: ", values_from_match(matches2))


     
