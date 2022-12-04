from aoc import aoc

moves = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}
scores = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}
# 6 = win, 3 = draw, 0 = lose
# x=me, y=them
outcome = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3]]


def get_score(them, me):
    my_move = moves[me]
    their_move = moves[them]
    return scores[my_move] + outcome[scores[their_move] - 1][scores[my_move] - 1]


def add_scores(data):
    goes = [row.split(" ") for row in data]
    return sum([get_score(*row) for row in goes])


map_outcome_to_score = {
    "X": 0,
    "Y": 3,
    "Z": 6
}


def add_scores2(data):
    goes = [row.split(" ") for row in data]
    return sum([get_score(g[0], get_move(*g)) for g in goes])


def get_move(their_move, winlosedraw):
    scoreneeded = map_outcome_to_score[winlosedraw]
    them = moves[their_move]  # name of their move
    rowno = scores[them] - 1  # row in matrix
    moveneeded = outcome[rowno].index(scoreneeded)
    return "ABC"[moveneeded]


def run(file):
    print("Part 1")
    data = aoc.loadlines(file)
    print(add_scores(data))
    print("Part 2")
    print(add_scores2(data))


if __name__ == "__main__":
    print("Test Data")
    run("test.txt")
    print("Actual Data")
    run("data.txt")
