#=
day6:
- Julia version: 
- Author: mike.downey
- Date: 2022-12-06
=#
 
data = read(open("day_06/data.txt"))

function aretheyunique(letters)
    s = Set([l for l in letters])
    return length(s) == length(letters)
end


function get_marker(word, len)
    for i in range(1, length(word))
        if aretheyunique(word[i : i + len - 1]) # remember index starts at 1 so
            return i + len - 1 # skip 'len' and report first char after 'start' marker
        end
    end
end

# Part 1
println("Part 1")
println(get_marker(data, 4))

# Part 2
println("Part 2")
println(get_marker(data, 14))
