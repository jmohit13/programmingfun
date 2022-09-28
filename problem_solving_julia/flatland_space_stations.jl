# Enter your code here

first_multiple_input = Array{String}(split(rstrip(readline())))
n = parse(Int64, first_multiple_input[1])
c = parse(Int64, first_multiple_input[2])
second_multiple_input = Array{String}(split(rstrip(readline())))
println(n, c, second_multiple_input)

function flatlandSpaceStations!(out, n, c)
    sorted_stations = sort(c, rev=true)
    println(sorted_stations)
end

flatlandSpaceStations!(n,second_multiple_input)

first_multiple_input = Array{String}(split(rstrip(readline(STDIN))))
