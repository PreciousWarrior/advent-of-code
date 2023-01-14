n = 3

elves = [elf.split("\n") for elf in open("1.txt").read().split('\n\n')]
calorie_sums = []

for i, elf in enumerate(elves):
    calorie_sums.append(0)
    for food in elf:
        if food == "":
            continue
        calorie_sums[i] += int(food)

calorie_sums.sort(reverse=True)
print(sum(calorie_sums[0:n]))

