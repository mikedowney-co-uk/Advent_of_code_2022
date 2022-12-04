#=
day2:
- Julia version: 
- Author: mike.downey
- Date: 2022-12-04

This version is very similar to the original python code.
=#

# file = open("day_02/test.txt")
file = open("day_02/data.txt")
data = readlines(file)

# Part 1
println("Part 1")

outcome = [
    [3 6 0],
    [0 3 6],
    [6 0 3]]

moves = Dict(
    "A" => "rock",
    "B" => "paper",
    "C" => "scissors",
    "X" => "rock",
    "Y" => "paper",
    "Z" => "scissors"
)

scores = Dict(
    "rock" => 1,
    "paper" => 2,
    "scissors" => 3
)

function get_score(them, me)
    my_move = moves[me]
    their_move = moves[them]
    return scores[my_move] + outcome[scores[their_move]][scores[my_move]]
end

function split_lines(lines, separator)
    output = []
    for line in lines
        println(line)
        row = split(line, separator)
        push!(output, row)
    end
    return output
end

function add_scores(lines)
    score = 0
    for row in lines
        if length(row)>0
            l = split(row, " ")
            score += get_score(l[1], l[2])
        end
    end
    return score
end

println(add_scores(data))

# Part 2
println("Part 2")

map_outcome_to_score = Dict(
    "X"=> 0,
    "Y"=> 3,
    "Z"=> 6
)

function get_move(their_move, winlosedraw)
    scoreneeded = map_outcome_to_score[winlosedraw]
    them = moves[their_move]  # name of their move
    rowno = scores[them]  # row in matrix
    moveneeded = findfirst(isequal(scoreneeded), outcome[rowno])
    # Returns a 'CartesianIndex' which we can use to extract from an array but not a string.
    return ["A" "B" "C"][moveneeded]
end

score = 0
for row in data
    global score
    r = split(row, " ")
    move = get_move(r[1], r[2])
    score += get_score(r[1], move)
end

println(score)