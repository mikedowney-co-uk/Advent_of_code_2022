#=
day10:
- Julia version: 
- Author: mike.downey
- Date: 2022-12-10
=#
import Test

data1 = readlines(open("day_10/test.txt"))
data2 = readlines(open("day_10/data.txt"))

# Unlike the Python version, where I started with the Cpu and extended it
# for the display, here I am going to create a single structure to hold
# both bits.
mutable struct Cpu
    x::Int
    cycle::Int
    data::Array{String}
    strengths::Dict{Int,Int}
    row::Array{String}
    display::Array{String}

    function Cpu(data::Array{String})
        this = new()
        this.x = 1
        this.cycle = 1
        this.data = data
        this.strengths = Dict()
        this.row = []
        this.display = []
        return this
    end
end

function inc(cpu::Cpu)
    cpu.strengths[cpu.cycle] = cpu.cycle * cpu.x
    cpu.cycle = cpu.cycle + 1
end

function execute(cpu::Cpu, instruction::String, command::Function)
    command(cpu)
    if instruction != "noop"
        command(cpu)
        inst,value = split(instruction, " ")
        cpu.x = cpu.x + parse(Int, value)
    end
end

test = Cpu(data1)
Test.@test test.cycle == 1
execute(test, "noop", inc)
Test.@test test.cycle == 2
execute(test, "addx 10", inc)
Test.@test test.x == 11

function run(cpu::Cpu, command::Function)
    for instruction in cpu.data
        execute(cpu, instruction, command)
    end
end

function part1(data)
    cpu = Cpu(data)
    run(cpu, inc)
    result = sum([cpu.strengths[a] for a in [20,60,100,140,180,220]])
    println(result)
    return result
end

# version of 'inc' for the display
function display(cpu)
    pixel = (cpu.cycle - 1) % 40
    if abs(pixel - cpu.x) <= 1
        push!(cpu.row, "#")
    else
        push!(cpu.row, " ")
    end
    if pixel == 39
        push!(cpu.display, string(cpu.row...))
        cpu.row = []
    end
    cpu.cycle = cpu.cycle + 1
end

function part2(data)
    cpu = Cpu(data)
    run(cpu, display)
    for row in cpu.display
        println(row)
    end
end

# Part 1
println("Part 1")
result = part1(data1)
Test.@test result == 13140

result = part1(data2)
Test.@test result == 14040

# Part 2
println("Part 2")
part2(data1)
println()
part2(data2)