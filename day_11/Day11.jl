#=
Day11:
- Julia version: 
- Author: mike.downey
- Date: 2022-12-11
=#
import Test

counter = 0
factors = 0

mutable struct Monkey
    monkey::Int
    items::Array{Int}
    add::Int
    mul::Int
    power::Int
    test::Int
    whentrue::Int
    whenfalse::Int
    inspected::Int

    function Monkey(items::Array{Int}, operation::String, number,
            test::Int, whentrue::Int, whenfalse::Int)
        global counter
        this = new()
        this.monkey = counter
        counter = counter + 1
        this.whentrue = whentrue
        this.whenfalse = whenfalse
        this.items = items

        if operation == "+"
            this.add = number
            this.mul = 1
            this.power = 1
        elseif operation == "*"
           this.power = 1
           this.add = 0
           this.mul = number
        else
            this.power = number
            this.add = 0
            this.mul = 1
        end
        return this
    end
end

function worry(monkey::Monkey)
    if monkey.power > 1
        level = monkey.items[0] * monkey.items[0]
    else
        level = (monkey.items[0] + monkey.add) * monkey.mul
    end
    monkey.items[0] = level
    monkey.inspected = monkey.inspected + 1
end

function dotest(monkey::Monkey)
    if monkey.items[0] % monkey.test
        return monkey.whentrue
    else
        return monkey.whenfalse
    end
end

function throw(monkey::Monkey)
    return popfirst!(monkey.items)
end

function receive(monkey::Monkey, item)
    push!(monkey.items, item)
end

function phew(monkey::Monkey)
    monkey.items[0] = div(monkey.items[0], 3)
end

function load_monkeys(file)
    data = readlines(file)
    monkeys::Array{Monkey} = []
    counter = 0

    while length(data) > 0
        popfirst!(data)
        line = popfirst!(data)
        x, items = split(line, ":")
        items = [parse(Int, i) for i in split(items, ",")]

        line = popfirst!(data)
        op = split(line, "= old ")[2]
        if occursin("* old", op)
            operand = 2
            operation = "^"
        elseif occursin("*", op)
            operand = parse(Int, split(op, "* ")[2])
            operation = "*"
        else
            operand = parse(Int, split(op, "+ ")[2])
            operation = "+"
        end
        line = popfirst!(data)
        test = parse(Int, split(line, "by ")[2])

        line = popfirst!(data)
        tru = parse(Int, split(line, "monkey ")[2])

        line = popfirst!(data)
        fals = parse(Int, split(line, "monkey ")[2])

        monkey = Monkey(items, operation, operand, test, tru, fals)
        push!(monkeys, monkey)
        println(monkey)
        if length(data)>0
            popfirst!(data)
        end
    end
    return monkeys
end


function action(monkey::Monkey, monkeys::Array{Monkey}, relax::Function)
    if length(monkey.items) == 0
        return false
    end
    worry(monkey)
    
# Part 1
println("Part 1")
monkeys = load_monkeys("day_11/test.txt")
# Test.@test result == expected

# Part 2
println("Part 2")
