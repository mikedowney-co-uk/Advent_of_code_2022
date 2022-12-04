#=
day3:
- Julia version: 
- Author: mike.downey
- Date: 2022-12-04
=#

# file = open("day_03/test.txt")
file = open("day_03/data.txt")
data = readlines(file)

# Part 1
println("Part 1")

# Pass a Char (not a String) and get the priority
function priority(letter)
    asc = 1 + Int(letter) - Int('a')
    if asc > 0
        return asc
    else
        return 27 + Int(letter) - Int('A')
    end
end

function halves(contents)
    return [contents[begin:div(length(contents),2)], contents[1+div(length(contents),2):end]]
end

# Returns a set of Char
s2c = s -> s[1]
function string2set(contents)
    letters = split(contents,"")
    chars = s2c.(letters) # dot notation applies function to elements of an array
    return Set(chars)
end

function get_in_common(row)
    half = halves(row)
    return intersect(string2set(half[1]), string2set(half[2]))
end

function get_priority_for_common(row)
    return sum(priority.(get_in_common(row)))
end

println(sum(get_priority_for_common.(data)))

# Part 2
# Group into blocks of 3 and find their badge types, sum those.
println("Part 2")

function find_badge_and_priority(elves)
    allhave = intersect(elves[1], elves[2], elves[3])
    return priority(collect(allhave)[1])
end

priorities = [find_badge_and_priority(data[i:i+2]) for i in range(1, length(data), step=3)]
println(sum(priorities))
