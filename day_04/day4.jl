#=
day4:
- Julia version: 
- Author: mike.downey
- Date: 2022-12-04
=#

#file = open("day_04/test.txt")
file = open("day_04/data.txt")
data = readlines(file)

# Part 1
println("Part 1")

function set_from_range(a,b)
    return Set(collect(range(parse(Int, a),parse(Int, b))))
end

function set_from_data(s)
    a,b = split(s, "-")
    return set_from_range(a, b)
end

function get_jobs(row)
    elf1,elf2 = split(row, ",")
    return set_from_data(elf1), set_from_data(elf2)
end

function one_is_subset(set1, set2)
    common = intersect(set1, set2)
    return length(common) == length(set1) || length(common) == length(set2)
end


count = 0
for row in data
    global count
    elf1,elf2 = get_jobs(row)
    if one_is_subset(elf1, elf2)
        count += 1
    end
end
println(count)

# Part 2
println("Part 2")
count = 0
for row in data
    global count
    elf1,elf2 = get_jobs(row)
    if length(intersect(elf1, elf2)) > 0
        count += 1
    end
end
println(count)