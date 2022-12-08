#=
day8:
- Julia version: 
- Author: mike.downey
- Date: 2022-12-08

Added some tests to the code so I can check that I haven't broken anything
while working on it/refactoring etc.
=#

import Test

mutable struct Forest
    height::Int
    width::Int
    trees::Array{Int, 2}

    function Forest(data::Array{String})
        this = new()
        this.height = length(data)
        this.width = length(data[1])
        arrayofarrays = [row2ints(row) for row in data]
        # Convert an array of arrays into a Matrix
        # Don't underatand this yet. Found it on Stackoverflow
        this.trees = vcat(transpose.(arrayofarrays)...)
        #=
        What it seems to do:
        transpose.(a) the . calls transpose on each 'row' in the array instead of just once on the
        whole array.
        vcat( ...) the ... splits the output of transpose into elements and passes the to vcat
        which combines them into a matrix.
        =#
        return this
    end
end

row2ints(line) = [parse(Int, t) for t in split(line,"")]


function count(forest::Forest)
    count = 0
    for y in range(1,forest.height)
        for x in range(1,forest.width)
            count += isvisible(forest, x, y)
        end
    end
    return count
end

function count_in_direction(tree, trees, direction)
    l = length(trees)
    if direction == 1
        for i in range(1,l)
            if trees[i] >= tree
                return i
            end
        end
    end
    if direction == -1
        for i in range(1,l)
            if trees[1 + l - i] >= tree
                return i
            end
        end
    end
    return length(trees)
end

function scenic_score(forest::Forest, x::Int, y::Int)
    row = forest.trees[y, :]
    column = forest.trees[:, x]
    tree = forest.trees[y, x]
    return (
            count_in_direction(tree, row[x + 1:end], 1) *
            count_in_direction(tree, row[1:x-1], -1) *
            count_in_direction(tree, column[y + 1:end], 1) *
            count_in_direction(tree, column[1:y-1], -1)
    )
end

function check_row(x::Int, row)
    tree = row[x]
    return (all([t < tree for t in row[1:x - 1]]) || all([t < tree for t in row[x + 1:end]]))
end

function check_column(y::Int, column)
    tree = column[y]
    return (all([t < tree for t in column[1:y - 1]]) || all([t < tree for t in column[y + 1:end]]))
end

function isvisible(forest::Forest, x::Int, y::Int)
    row = forest.trees[y, :]
    column = forest.trees[:, x]
    if x == 1 ||  y == 1 || x == forest.width || y == forest.height ||
            check_row(x, row) || check_column(y, column)
        return 1
    else
        return 0
    end
end

function max_scenic(forest::Forest)
    score = 0
    for y in range(1, forest.height)
        for x in range(1, forest.width)
            score = max(score, scenic_score(forest, x, y))
        end
    end
    return score
end

# The test data set
testdata = readlines(open("day_08/test.txt"))
forest = Forest(testdata)

Test.@test count_in_direction(5, [5, 3, 3], -1) == 3
Test.@test count_in_direction(5, [1, 5, 3], 1) == 2
Test.@test count(forest) == 21
Test.@test scenic_score(forest, 2, 3) == 6
Test.@test max_scenic(forest) == 8


# The test data
forest = Forest(readlines(open("day_08/data.txt")))

# Part 1
println("Part 1")
println(count(forest))


# Part 2
println("Part 2")
println(max_scenic(forest))