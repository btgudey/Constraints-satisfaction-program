# Nairobi CSP Map Coloring

colors = ["Blue", "Red", "Green", "Yellow"]

graph = {
    "Westlands": ["Starehe", "Dagoretti North", "Kibra"],
    "Dagoretti North": ["Westlands", "Dagoretti South", "Kibra"],
    "Dagoretti South": ["Dagoretti North", "Langata", "Kibra"],
    "Langata": ["Dagoretti South", "Kibra"],
    "Kibra": ["Westlands", "Dagoretti North", "Dagoretti South", "Langata"],

    "Roysambu": ["Kasarani", "Ruaraka"],
    "Kasarani": ["Roysambu", "Ruaraka", "Embakasi North"],
    "Ruaraka": ["Roysambu", "Kasarani", "Mathare"],

    "Embakasi South": ["Embakasi Central", "Embakasi East"],
    "Embakasi North": ["Kasarani", "Embakasi Central"],
    "Embakasi Central": ["Embakasi North", "Embakasi South", "Embakasi East"],
    "Embakasi East": ["Embakasi Central", "Embakasi West"],
    "Embakasi West": ["Embakasi East"],

    "Makadara": ["Kamukunji", "Starehe"],
    "Kamukunji": ["Makadara", "Starehe", "Mathare"],
    "Starehe": ["Westlands", "Makadara", "Kamukunji", "Mathare"],
    "Mathare": ["Ruaraka", "Kamukunji", "Starehe"]
}

assignment = {}

def is_valid(region, color):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def solve(regions):
    if not regions:
        return True

    region = regions[0]

    for color in colors:
        if is_valid(region, color):
            assignment[region] = color

            if solve(regions[1:]):
                return True

            del assignment[region]

    return False


regions = list(graph.keys())

if solve(regions):
    print("Nairobi Coloring Solution:")
    for r, c in assignment.items():
        print(r, "->", c)
else:
    print("No solution found with given colors")
  
