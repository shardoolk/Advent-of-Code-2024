### Day5" --- Day 5: Print Queue ---
import functools
rules, orders = open("input_day5.txt").read().strip().split("\n\n")

rules = rules.split("\n")

rulesSet = []
for rule in rules:
    rulesSet.append(list(map(int, rule.split("|"))))

cache = {}

for x, y in rulesSet:
    cache[(x, y)] = True
    cache[(y, x)] = False


def validOrder(order):
    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            key = (order[i], order[j])
            if key in cache and not cache[key]:
                return False
            
    return True

total = 0
for order in orders.split("\n"):
    order = list(map(int, order.split(",")))
    if validOrder(order):
        total += order[len(order) // 2]       
        

      
print("Part1 soluton : ", total)     


cache_pt2  = {}

for x, y in rulesSet:
    cache_pt2[(x, y)] = -1
    cache_pt2[(y, x)] = 1
    

def validOrder2(order):
    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            key = (order[i], order[j])
            if key in cache_pt2 and cache_pt2[key] == 1:
                return False
    return True


def compare(x,y):
    return cache_pt2.get((x, y), 0)

part2_total = 0

for order in orders.split("\n"):
    order = list(map(int, order.split(",")))
    if validOrder2(order):
        continue
    order.sort(key=functools.cmp_to_key(compare))
    part2_total += order[len(order) // 2]    
    
    
print("Part2 solution : ", part2_total)    
