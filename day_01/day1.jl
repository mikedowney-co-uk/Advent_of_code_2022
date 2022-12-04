#=
day1:
- Julia version: 
- Author: mike.downey
- Date: 2022-12-04
=#

# file = open("day_01/test.txt")
file = open("day_01/data.txt")
data = readlines(file)

# Part 1

function count(testdata)
    highest = [0, 0] # Elf and calories
    elf::Int = 1
    total_calories::Int = 0
    for cals in testdata
        if length(cals) > 0
            calories = parse(Int, cals)
            total_calories += calories
        else
            if total_calories > highest[2]
                highest = [elf, total_calories]
            end
            elf += 1
            total_calories = 0
        end
    end
    return highest
end

highest = count(data)
println("Elf ",highest[1]," has most calories: ",highest[2])

# Part 2
# Need to keep record of the top 3 elves
function countall(testdata)
    all = []
    total_calories::Int = 0
    for cals in testdata
        if length(cals) > 0
            calories = parse(Int, cals)
            total_calories += calories
        else
            push!(all, total_calories)
            total_calories = 0
        end
    end
    return all
end

allcals = countall(data);

#=
Get the top 3, Can either use
sorted = sort(allcals, lt=(x,y)->isless(y, x));
cals = [top for top in  first(sorted ,3)]
to sort in reverse order then get the first elements, or as below, sorting in normal
order then getting the last elements.
=#

sorted = sort(allcals)
cals = [top for top in  last(sorted ,3)]
println(sum(cals))
