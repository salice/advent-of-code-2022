def score_val(letter):
    score_str = "abcdefghijklmnopqrstuvwxyz"
    score = score_str.index(letter) + 1 if letter in score_str \
            else score_str.index(letter.lower()) + 27
    return score

def part_a(input_path):
    f = open(input_path).read()
    data = [i for i in f.strip().split("\n")]
    final_score = 0
    for bag in data:
        left = list(set(bag[:len(bag) // 2]))
        right = list(set(bag[len(bag) // 2:]))
        dupe = [i for i in left if i in right][0]    
        final_score += score_val(dupe)
    return final_score

def part_b(input_path):
    f = open(input_path).read()
    data = [i for i in f.strip().split("\n")]
    groups = [data[i * 3:(i+1) * 3] for i in range((len(data) + 2) // 3)]
    final_score = 0
    for trio in groups:
        a, b, c = trio
        a = list(set(a))
        b = list(set(b))
        c = list(set(c))
        dupe = [i for i in a if i in b and i in c][0]
        final_score += score_val(dupe)
    return final_score

if __name__ == "__main__":
    input_path = "input/input3.txt"
    soln_a = part_a(input_path)
    print(f"part a solution is: {soln_a}")
    soln_b = part_b(input_path)
    print(f"part b solution is: {soln_b}")