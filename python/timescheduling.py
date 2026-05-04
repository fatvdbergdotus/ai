from z3 import *

# -----------------------------
# Data
# -----------------------------
courses = ["Math", "Physics", "CS", "Biology"]

slots = ["9AM", "11AM", "1PM"]
rooms = ["R1", "R2"]

teachers = {
    "Math": "Alice",
    "Physics": "Bob",
    "CS": "Alice",
    "Biology": "Carol"
}

# Conflicts (shared students)
conflicts = [
    ("Math", "Physics"),
    ("Physics", "CS")
]

# -----------------------------
# Encode variables
# -----------------------------
# Each course has:
# - slot index
# - room index

slot_vars = {c: Int(f"{c}_slot") for c in courses}
room_vars = {c: Int(f"{c}_room") for c in courses}

solver = Solver()

# -----------------------------
# Domain constraints
# -----------------------------
for c in courses:
    solver.add(slot_vars[c] >= 0, slot_vars[c] < len(slots))
    solver.add(room_vars[c] >= 0, room_vars[c] < len(rooms))

# -----------------------------
# Constraint 1: No teacher conflict
# -----------------------------
for c1 in courses:
    for c2 in courses:
        if c1 != c2 and teachers[c1] == teachers[c2]:
            solver.add(slot_vars[c1] != slot_vars[c2])

# -----------------------------
# Constraint 2: No room conflict
# -----------------------------
for c1 in courses:
    for c2 in courses:
        if c1 != c2:
            solver.add(
                Or(
                    slot_vars[c1] != slot_vars[c2],
                    room_vars[c1] != room_vars[c2]
                )
            )

# -----------------------------
# Constraint 3: Student conflicts
# -----------------------------
for c1, c2 in conflicts:
    solver.add(slot_vars[c1] != slot_vars[c2])

# -----------------------------
# Solve
# -----------------------------
if solver.check() == sat:
    model = solver.model()
    
    print("\nTimetable:\n")
    for c in courses:
        s = model[slot_vars[c]].as_long()
        r = model[room_vars[c]].as_long()
        print(f"{c:8} → {slots[s]} in {rooms[r]}")
else:
    print("No solution found")


'''
Output: 

Timetable:

Math     → 9AM in R1
Physics  → 11AM in R1
CS       → 1PM in R1
Biology  → 11AM in R2
'''
