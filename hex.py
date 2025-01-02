import random
import pandas as pd
import json


# Load the JSON file
with open(r'C:\Users\Xcient\Desktop\Rl code\neigbhors.json', "r") as file:
    data = json.load(file)

# Access only the "neighbor" key
map_placements = data["map_placements"]
neighbors = data["neighbor"]
# print(neighbors)


# Define the fields and their respective counts
fields = (
    ["Forest"] * 4 +
    ["Goat Farm"] * 4 +
    ["Grain"] * 4 +
    ["Ore"] * 3 +
    ["Brick"] * 3 +
    ["Desert"]
)


# Shuffle the fields to randomize placement
random.shuffle(fields)

# Define the number distribution as per Catan rules
numbers = [2, 12, 7] + [i for i in range(3, 12) for _ in range(2) if i != 7] # Single 2 & 12, pairs of 3–11
random.shuffle(numbers)

# # Assign numbers and fields to map placements
for placement, field in zip(map_placements.values(), fields):
    # Handle the "Desert" case first
    if field == "Desert":
        placement[7] = "Desert"  # Always assign 7 to Desert
    else:
        # Assign the next number to this placement
        while True:
            assigned_number = numbers.pop(0)
            if assigned_number != 7:  # Ensure 7 isn't assigned to non-desert fields
                placement[assigned_number] = field
                break


# for placement_name, placement_data in map_placements.items():
#     # Get the last key-value pair
#     last_key, last_value = list(placement_data.items())[-1]
#     # Print in the required format
#     print(f"{placement_name} = {last_key}: '{last_value}'")


# Add logic to generate road placement options
for map_key, tile_data in map_placements.items():
    for position, value in tile_data.items():
        # print(value)
        if "settlement" in str(value) :
            print(f"{position} : {neighbors[position]}\nChecking Availabity")
            for pos in neighbors[position]:
                # for key, val  in map_placements.items():
                try:
                    chk = tile_data[pos]
                    if chk != 0:
                        print(f"{pos} : Taken")
                    else: 
                        print(f"{pos} : Vaccent")
                except:
                    print(f"{pos} not available in this {map_key}")
