#=
day5:
- Julia version: 
- Author: mike.downey
- Date: 2022-12-05
=#
 
data = readlines(open("day_05/data.txt"))

# Split the input into stacks and move instructions
function parse_input(data)
    stacks = []
    moves = []
    part = 0
    for line in data
        if line == ""
            part += 1
            continue
        elseif part == 0
            push!(stacks, line)
        else
            push!(moves, line)
        end
    end
    return stacks,moves
end

remove_char(stacks, howmany) = [s[1 + howmany:end] for s in stacks]
get_leftmost_stack(stacks) = [s[1] for s in stacks if s[1] != ' ']


function build_stacks(stacks)
    cratestacks = []
    while length(stacks[length(stacks)]) > 0
        stacks = remove_char(stacks,1)
        push!(cratestacks, get_leftmost_stack(stacks))
        stacks = remove_char(stacks,3)
    end
    return cratestacks
end

function move_one(cratestacks, wherefrom, whereto)
    crate = popfirst!(cratestacks[wherefrom])
    pushfirst!(cratestacks[whereto], crate)
end

get_moves(instruction) = match(r"(\d+).*(\d+).*(\d+)", instruction).captures

function move_many(cratestacks, wherefrom, whereto, howmany)
    newstack = cratestacks[wherefrom][1:howmany]
    cratestacks[wherefrom] = cratestacks[wherefrom][1 + howmany:end]
    newstack = vcat(newstack, cratestacks[whereto])
    cratestacks[whereto] = newstack
end

# Part 1
println("Part 1")
stacks,moves = parse_input(data)
cratestacks = build_stacks(stacks)
instructions = [[parse(Int, i) for i in get_moves(m)] for m in moves]
for move in instructions
    for i in range(1, move[1])
        move_one(cratestacks, move[2], move[3])
    end
end
println([popfirst!(c) for c in cratestacks])


# Part 2
println("Part 2")
stacks,moves = parse_input(data)
cratestacks = build_stacks(stacks)
for move in instructions
    move_many(cratestacks, move[2], move[3],move[1])
end
println([popfirst!(c) for c in cratestacks])
