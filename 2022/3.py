def get_priority(character):
    code = ord(character)
    if code <= ord("Z"):
        return code-ord("A")+27
    return code-ord("a")+1

rucksacks = open("3.txt").read().split("\n")[0:-1]
def p1():
    total = 0
    for rucksack in rucksacks:
        c1 = rucksack[0:len(rucksack)//2]
        c2 = rucksack[len(rucksack)//2:]
        duplicate = list(filter(lambda item: item in c2, c1))[0]
        total += get_priority(duplicate)
    return total
def p2():
    total = 0
    for i in range(0, len(rucksacks), 3):
        group = [rucksacks[i], rucksacks[i+1], rucksacks[i+2]]
        group = [set([*sack]) for sack in group]
        badge = set.intersection(*group).pop()
        total += get_priority(badge)
    return total

print(p2())

