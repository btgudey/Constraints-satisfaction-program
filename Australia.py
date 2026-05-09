# Australia Map Coloring CSP

colors = ["Blue", "Red", "Green"]

# Graph (adjacency list)
graph = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA"]
}

# Store assignment
assignment = {}

def is_valid(region, color):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def solve(region_list):
    if not region_list:
        return True

    region = region_list[0]

    for color in colors:
        if is_valid(region, color):
            assignment[region] = color

            if solve(region_list[1:]):
                return True

            del assignment[region]

    return False


regions = list(graph.keys())

if solve(regions):
    print("Solution Found:")
    for r in assignment:
        print(r, "->", assignment[r])
else:
    print("No solution")
