regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["SA", "Q", "V"],
    "V": ["SA", "NSW"],
    "T": []
}

colors = ["Red", "Green", "Blue"]

def is_valid(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve(assignment):
    if len(assignment) == len(regions):
        return assignment

    # Pick next unassigned region
    for region in regions:
        if region not in assignment:
            break

    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color

            result = solve(assignment)
            if result:
                return result

            del assignment[region]

    return None

solution = solve({})
print("Solution:", solution)

# Output:
# Solution: {'WA': 'Red', 'NT': 'Green', 'SA': 'Blue', 'Q': 'Red', 'NSW': 'Green', 'V': 'Red', 'T': 'Red'}
