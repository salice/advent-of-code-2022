
vals = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
    "win": 6,
    "lose": 0,
    "tie": 3
}

def part_a(input_path):
    f = open(input_path).read()
    data = [i for i in f.strip().split("\n")]
    score = 0
    for game in data:
        opponent, me = game.split(" ")
        if vals[opponent] == vals[me]:
            score += vals[me] + vals["tie"]
        elif opponent == "A":
            if me == "Y":
                score += vals["Y"] + vals["win"]
            else:
                score += vals["Z"] + vals["lose"]
        elif opponent == "B":
            if me == "X":
                score += vals["X"] + vals["lose"]
            else:
                score += vals["Z"] + vals["win"]
        else:
            if me == "X":
                score += vals["X"] + vals["win"]
            else:
                score += vals["Y"] + vals["lose"]
    return score

vals_b = {
    "A": 1,
    "B": 2,
    "C": 3,
    "lose": 0,
    "tie": 3,
    "win": 6

}
def part_b(input_path):
    f = open(input_path).read()
    data = [i for i in f.strip().split("\n")]
    score = 0
    for game in data:
        opponent, outcome = game.split(" ")
        if outcome == "Y":
            score += vals_b[opponent] + vals_b["tie"]
        elif outcome == "X":
            if opponent == "A":
                score += vals_b["lose"] + vals_b["C"]
            elif opponent == "B":
                score += vals_b["lose"] + vals_b["A"]
            else:
                score += vals_b["lose"] + vals_b["B"]
        else:
            if opponent == "A":
                score += vals_b["win"] + vals_b["B"]
            elif opponent == "B":
                score += vals_b["win"] + vals_b["C"]
            else:
                score += vals_b["win"] + vals_b["A"]
        print(f"{game}: {score}")
    print(score)
    return score

    


if __name__ == "__main__":
    input_path = "input/input2a.txt"
    # input_path = "input/test2.txt"
    soln_a = part_a(input_path)
    print(f"part a solution is: {soln_a}")
    soln_b = part_b(input_path)
    print(f"part b solution is: {soln_b}")