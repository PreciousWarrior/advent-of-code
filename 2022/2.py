def winning_points(opponent, me):
    if opponent == "A":
        if me == "X": return 3
        if me == "Y": return 6
    if opponent == "B":
        if me == "Y": return 3
        if me == "Z": return 6
    if opponent == "C":
        if me == "Z": return 3
        if me == "X": return 6
    return 0

def shape_points(me):
    mapping = {"X": 1, "Y": 2, "Z": 3}
    return mapping[me]

def winning_points_p2(me):
    mapping = {"X": 0, "Y": 3, "Z": 6}
    return mapping[me]

def shape_points_p2(opponent, me):
    if opponent == "A":
        if me == "X": return 3
        if me == "Y": return 1
        return 2
    if opponent == "B":
        if me == "X": return 1
        if me == "Y": return 2
        return 3
    if me == "X": return 2
    if me == "Y": return 3
    return 1

total = 0
strategies = open("2.txt").read().split("\n")[:-1]
for strategy in strategies:
    [opponent, me] = [strategy.split(" ")[0], strategy.split(" ")[1]]
    #total += shape_points(me) + winning_points(opponent, me)
    total += shape_points_p2(opponent, me) + winning_points_p2(me)
print(total)
