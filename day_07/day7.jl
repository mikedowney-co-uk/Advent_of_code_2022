#=
day7:
- Julia version: 
- Author: mike.downey
- Date: 2022-12-07

This is based on the first attempt in python, not the modified more object-oriented
version given here.
=#
 
data = readlines(open("day_07/data.txt"))

# Nodes holding the files and directories
mutable struct FileTree
    name::String
    size::Int
    children::Dict
    parent::FileTree
    path::String

    function FileTree(path::Array{String}, name::String, size::Int=0)
        this = new()
        this.children = Dict()
        this.name = name
        this.size = size
        this.parent = this
        this.path = string(join("/",path), name)
        return this
    end
end

function addnode(this::FileTree, node::FileTree)
    this.children[node.name] = node
    node.parent = this
end

getchild(this::FileTree, name::String) = this.children[name]

path = [""]
root = FileTree(path, "/")
cnode = root

function cd(p::String)
    global path, cnode
    if p == "/"
        path = ["/"]
        cnode = root
        return
    end
    if p == ".."
        pop!(path)
        cnode = cnode.parent
        return
    end
    push!(path, p)
    cnode = getchild(cnode, p)
end

for line in data
    bits = split(line," ")
    if bits[1] == "\$"
        if bits[2] == "cd"
            cd(string(bits[3]))
        end
        continue
    end
    # within the output of 'ls'
    fileinfo = parse(Int, replace(string(bits[1]), "dir" => "0"))
    name = string(bits[2])
    newnode = FileTree(path, name, fileinfo)
    addnode(cnode, newnode)
end

sizes = Dict()

function getsize(node::FileTree)
    global sizes
    if node.size != 0
        return node.size
    end
    childsizes = [getsize(n) for n in values(node.children)]
    s = sum(childsizes)
    sizes[node.path] = s
    return s
end

rootsize = getsize(root)
println(rootsize)

# Part 1
println("Part 1")
# Dicts iterate Pairs which can be accessed using .first and .second
total = sum([s.second for s in sizes if s.second<100000])
println(total)

# Part 2
println("Part 2")
unused = 70000000 - sizes["//"]
needtofree = 30000000 - unused
# println(needtofree)
dirs = [s for s in sizes if s.second > needtofree]
second(dir::Pair) = dir.second
sorted = sort(dirs, by=second)
println(sorted[1].second)