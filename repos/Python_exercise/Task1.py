aircraft = { 8:5 ,9:7 ,6:1, 7:8, 1:8, 7:3, 8:2, 5:4 ,2:7}

print("Aircraft coordinates:")
print("x-coordinate is:",list(aircraft.keys()))
print("y-coordinate is:",list(aircraft.values()))


# defined a dictionary named fleet
fleet = {"aircraft1":{10:2}, "aircraft2": { 7:5}, "aircraft3": { 5:10 }, "aircraft4": { 4:5 }, "aircraft5": { 8:4}}
print("\nAircraft 1 coordinates:")
print("x-coordinate is:",list(fleet["aircraft1"].keys()))
print("y-coordinate is:",list(fleet["aircraft1"].values()))

print("\nAircraft 2 coordinates:")
print("x-coordinate is:",list(fleet["aircraft2"].keys()))
print("y-coordinate is:",list(fleet["aircraft2"].values()))

print("\nAircraft 3 coordinates:")
print("x-coordinate is:",list(fleet["aircraft3"].keys()))
print("y-coordinate is:",list(fleet["aircraft3"].values()))

print("\nAircraft 4 coordinates:")
print("x-coordinate is:",list(fleet["aircraft4"].keys()))
print("y-coordinate is:",list(fleet["aircraft4"].values()))

print("\nAircraft 5 coordinates:")
print("x-coordinate is:",list(fleet["aircraft5"].keys()))
print("y-coordinate is:",list(fleet["aircraft5"].values()))
