#=
day9:
- Julia version: 
- Author: mike.downey
- Date: 2022-12-09
=#

import Test


function move(direction::Vector{Int}, head::Vector{Int}, tail::Vector{Int})
    new = head + direction
    return new, movetail(new, tail)
end

function movetail(head::Vector{Int}, tail::Vector{Int})
   difference = head - tail
   absolutedif = abs.(difference)
   distance = max(absolutedif...)
   if distance > 1 && absolutedif > [1,1]
       tail = tail + sign.(difference)
   elseif distance > 1
       tail = tail + [Int(ceil(e)) for e in difference/distance]
   end
   return tail
end

head = [1,3]
tail = [2,4]
step = [1,0]
head,tail = move(step, head, tail)
Test.@test tail == [2,4]
head,tail = move(step, head, tail)
Test.@test tail == [2,4]
head,tail = move(step, head, tail)
Test.@test tail == [3,3]
head,tail = move(step, head, tail)
Test.@test tail == [4,3]

function get_move(move)
    direction, step = split(move, " ")
    if direction == "U"
        vector = [0,1]
    elseif direction == "D"
        vector = [0,-1]
    elseif direction == "L"
        vector = [-1,0]
    elseif direction == "R"
        vector = [1,0]
    else
        error(move)
    end
    return vector, parse(Int, step)
end

Test.@test get_move("L 5") == ([-1,0], 5)
Test.@test get_move("R 2") == ([1,0], 2)
Test.@test get_move("D 3") == ([0,-1], 3)
Test.@test get_move("U 1") == ([0,1], 1)

data1 = readlines(open("day_09/test1.txt"))
data2 = readlines(open("day_09/test2.txt"))
data3 = readlines(open("day_09/data.txt"))

function part1(data)
    head = [0,0]
    tail = [0,0]

    visited = Set()
    for line in data
        vector,count = get_move(line)
        for i in range(1, count)
            head,tail = move(vector, head, tail)
            push!(visited, tail)
        end
    end
    println(length(visited))
    return length(visited)
end

function part2(data)
    visited = Set()
    rope = [[0,0] for i in range(1,10)]
    for line in data
        vector,count = get_move(line)
        for i in range(1, count)
            rope[1] = rope[1] + vector
            for j in range(2, 10)
                rope[j] = movetail(rope[j-1], rope[j])
            end
        push!(visited, rope[end])
        end
    end
    println(length(visited))
    return length(visited)
end


# Part 1
println("Part 1")
Test.@test part1(data1) == 13
Test.@test part1(data3) == 6197

# Part 2
println("Part 2")
Test.@test part2(data2) == 36
Test.@test part2(data3) == 2562
println("done")