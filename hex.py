import random

# Map placements dictionary
map_placements = {
    'Map_Placement_1': {"p_1": "Agent_settlement", "p_2": 0, "p_3": 0, "p_4": 0, "p_5": 0, "p_6": "Agent_road"},
    'Map_Placement_2': {"p_3": 0, "p_7": 0, "p_8": 0, "p_9": 0, "p_10": 0, "p_5": 0},
    'Map_Placement_3': {"p_8": 0, "p_11": 0, "p_12": 0, "p_13": 0, "p_14": 0, "p_9": 0},
    'Map_Placement_4': {"p_15": 0, "p_6": "Agent_settlement", "p_5": 0, "p_18": 0, "p_17": 0, "p_16": 0},
    'Map_Placement_5': {"p_5": 0, "p_4": 0, "p_10": 0, "p_20": 0, "p_19": 0, "p_18": 0},
    'Map_Placement_6': {"p_10": 0, "p_9": 0, "p_14": 0, "p_22": 0, "p_21": 0, "p_20": 0},
    'Map_Placement_7': {"p_14": 0, "p_13": 0, "p_25": 0, "p_24": 0, "p_23": 0, "p_22": 0},
    'Map_Placement_8': {"p_38": 0, "p_16": 0, "p_17": 0, "p_35": 0, "p_36": 0, "p_37": 0},
    'Map_Placement_9': {"p_17": 0, "p_18": 0, "p_19": 0, "p_33": 0, "p_34": 0, "p_35": 0},
    'Map_Placement_10':{"p_19": "Agent_settlement", "p_20": 0, "p_21": 0, "p_31": 0, "p_32": 0, "p_33": 0},
    'Map_Placement_11':{"p_21": 0, "p_22": 0, "p_23": 0, "p_29": 0, "p_30": 0, "p_31": 0},
    'Map_Placement_12':{"p_23": 0, "p_24": 0, "p_26": 0, "p_27": 0, "p_28": 0, "p_29": 0},
    'Map_Placement_13':{"p_36": 0, "p_35": 0, "p_34": 0, "p_41": 0, "p_40": 0, "p_39": 0},
    'Map_Placement_14':{"p_34": 0, "p_33": 0, "p_32": 0, "p_43": 0, "p_42": 0, "p_41": 0},
    'Map_Placement_15':{"p_32": 0, "p_31": 0, "p_30": 0, "p_45": 0, "p_44": 0, "p_43": 0},
    'Map_Placement_16':{"p_30": 0, "p_29": 0, "p_28": 0, "p_47": 0, "p_46": 0, "p_45": 0},
    'Map_Placement_17': {"p_40": 0, "p_41": 0, "p_42": 0, "p_52": 0, "p_53": 0, "p_54": 0},
    'Map_Placement_18': {"p_42": 0, "p_43": 0, "p_44": 0, "p_50": 0, "p_51": 0, "p_52": 0},
    'Map_Placement_19': {"p_44": "Agent_settlement", "p_45": 0, "p_46": 0, "p_48": 0, "p_49": 0, "p_50": 0}
}

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
numbers = [2, 12] + [i for i in range(3, 12) for _ in range(2)]  # Single 2 & 12, pairs of 3–11
random.shuffle(numbers)

# Assign numbers and fields to map placements
for placement, field in zip(map_placements.values(), fields):
    # Assign the next number to this placement
    assigned_number = numbers.pop(0)
    
    # Handle the case where the field is "Desert"
    if field == "Desert":
        assigned_number = 7  # Always assign 7 to Desert
    
    # Update the placement dictionary
    placement[assigned_number] = field

# Print the updated map placements
for key, value in map_placements.items():
    print(f"{key} : {value}")
    # for kel,val in value.items():
        # print(f"{kel} : {val}")



# Define a helper function to get neighboring positions
def get_neighbors(position):
    neighbor_map = {
        "p_44": ["p_45", "p_46"],
        "p_45": ["p_44", "p_46"],
        "p_46": ["p_45", "p_48"],
        "p_48": ["p_46", "p_49"],
        "p_49": ["p_48", "p_50"],
        "p_50": ["p_49", "p_44"],
    }
    return neighbor_map.get(position, [])

# Add logic to generate road placement options
for map_key, tile_data in map_placements.items():
    print(f"{map_key} : {tile_data}")
    
    for position, value in tile_data.items():
        if value == "Agent_settlement":
            neighbors = get_neighbors(position)
            road_options = [pos for pos in neighbors if tile_data.get(pos) == 0]
            print(f"Settlement at {position} can have roads at: {road_options}")