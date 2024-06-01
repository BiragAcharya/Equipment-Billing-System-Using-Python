# Function to display equipment details
def display_equipment(equipment_list):
    print("\n#======================== Available Stocks of Equipment ==========================#")
    print("===================================================================================")

    # Print column headers for the equipment details
    print(
        "{:<4} {:<35} {:<20} {:<12} {:<8}".format(
            "Id", "Equipment", "Brand", "Price ($)", "Quantity"
        )
    )
    # Print a separator line
    print("=" * 83)

    # Iterate through each equipment in the list and display its details
    for index, equipment in enumerate(equipment_list, start=1):
        print(
            "{:<4} {:<35} {:<20} {:<12} {:<8}".format(
                index,
                equipment["name"],
                equipment["brand"],
                equipment["price"],
                equipment["quantity"],
            )
        )

    # Print a separator line    
    print("=================================================================================="+"\n")  

# Function to read equipment data from a file
def read_equipment_data(file_name):
    equipment_data = []

    with open(file_name, "r") as file:
        # Iterate through each line in the file
        
        for line in file:
            # Split the line into components and create a dictionary for each equipment
            name, brand, price, quantity = line.strip().split(", ")
            equipment = {
                "name": name,
                "brand": brand,
                "price": price,
                "quantity": int(quantity),
            }
            equipment_data.append(equipment)   # Add the equipment dictionary to the list
    return equipment_data