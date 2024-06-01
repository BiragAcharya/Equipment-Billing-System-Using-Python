# Import the datetime module
import datetime

# Import the display_equipment function from the display module
from display import display_equipment

# Function to handle equipment rental
def rent_equipment(equipment_list):
    # Display the available equipment to the user
    display_equipment(equipment_list)

    try:
        # Get customer's name
        customer_name = input("Enter your name: ")

        # Get the current rental date and time
        rental_date = datetime.datetime.now()

        # Initialize a variable to keep track of the total rental amount
        total_rental_amount = 0

        # Initialize a list to store rental details for generating invoice
        rental_details_list = []

        while True:
            # Get the user's choice for the equipment to rent
            choice = int(input("Enter the Equipment Id you want to rent (or 0 to finish): ")) - 1

            # Check if the choice is valid or the user wants to finish
            if choice < -1 or choice >= len(equipment_list):
                print("Invalid choice.")
                continue
            elif choice == -1:
                break

            # Get the selected equipment
            equipment = equipment_list[choice]

            # Check if there is available quantity to rent
            if equipment["quantity"] > 0:
                # Get rental duration from user, ensuring it's a positive
                while True:
                    try:
                        rental_duration = int(
                            input(f"Enter rental duration in days for {equipment['name']} : ")
                        )
                        if rental_duration <= 0:
                            print("Rental duration must be a positive number.")
                        else:
                            break
                    except ValueError:
                        print("Please enter a valid number.")

                # Get the quantity to rent from user
                while True:
                    try:
                        quantity_to_rent = int(
                            input(f"Enter the quantity of {equipment['name']} you want to rent: ")
                        )
                        if quantity_to_rent <= 0:
                            raise ValueError("Quantity must be positive number")
                        if quantity_to_rent <= equipment["quantity"]:
                            break
                        else:
                            print("Not enough quantity available.")
                    except ValueError:
                        print("Please enter a valid positive number.")

                # Calculate rental periods and rental amount
                rental_periods = rental_duration // 5
                if rental_duration % 5 != 0:
                    rental_periods += 1
                rental_price_per_period = float(equipment["price"].replace("$", ""))
                rental_amount = rental_price_per_period * rental_periods * quantity_to_rent

                # Update equipment data after rental
                equipment["rented_to"] = customer_name
                equipment["rental_date"] = rental_date
                equipment["rented_qn"] = quantity_to_rent
                equipment["initial_quantity"] = equipment["quantity"]
                equipment["quantity"] -= quantity_to_rent

                total_rental_amount += rental_amount

                rental_details_list.append(
                    {
                        "equipment_name": equipment["name"],
                        "brand_name": equipment["brand"],
                        "rental_duration": rental_duration,
                        "quantity_rented": quantity_to_rent,
                        "rental_price_per_5_days": equipment["price"],
                        "total_amount": rental_amount,
                    }
                )

                print(f"\nRented {quantity_to_rent} {equipment['name']} for {rental_duration} days.")

            else:
                print(f"Sorry, {equipment['name']} is currently unavailable.")

        if total_rental_amount > 0:
            print("\nEquipment rented successfully!")
            print(f"Total rental amount: ${total_rental_amount:.2f}")

            # Write updated equipment data to the file
            with open("equipment.txt", "w") as equipment_file:
                for equip in equipment_list:
                    equipment_file.write(
                        f"{equip['name']}, {equip['brand']}, {equip['price']}, {equip['quantity']}\n"
                    )

            # Generate invoices
            generate_rental_invoices(customer_name, rental_date, rental_details_list, total_rental_amount)

        else:
            print("No equipment rented.")

    except ValueError:
        print("Invalid input. Please enter a valid value.")

def generate_rental_invoices(customer_name, rental_date, rental_details_list, total_rental_amount):
    invoice_name = f"{customer_name}_{rental_date.strftime('%Y-%m-%d_%H-%M-%S')}_rental_invoice.txt"
    with open(invoice_name, "w") as invoice_file:
        invoice_file.write("\n"+"________________________________________________________________")
        invoice_file.write("\n"+f"Date: {rental_date.strftime('%Y-%m-%d %H:%M:%S')}")
        invoice_file.write("\n"+"____________________    Rental Invoice     _____________________")
        invoice_file.write("\n"+"                                                                ")
        invoice_file.write("\n"+" ******************** Birag Equipment Store ********************")
        invoice_file.write("\n"+"    ---------------------Inaruwa,Nepal----------------------    ")
        invoice_file.write("\n"+"   PAN No. 77777                          Contact No.: 980010200")
        invoice_file.write("\n"+"----------------------------------------------------------------")
        invoice_file.write("\n"+f"Customer Name: {customer_name}")

        for idx, rental_details in enumerate(rental_details_list, start=1):
            invoice_file.write("\n\n"+"Transaction #" + str(idx) + ":")
            invoice_file.write("\n"+f"Equipment Name: {rental_details['equipment_name']}")
            invoice_file.write("\n"+f"Brand Name: {rental_details['brand_name']}")
            invoice_file.write("\n"+f"Rental Duration: {rental_details['rental_duration']} days")
            invoice_file.write("\n"+f"Quantity Rented: {rental_details['quantity_rented']}")
            invoice_file.write("\n"+f"Price per 5 days: {rental_details['rental_price_per_5_days']}")
            invoice_file.write("\n"+f"Total Amount: ${rental_details['total_amount']:.2f}")
            invoice_file.write("\n"+"-" * 64)

            invoice_file.write("\n\nTotal Rental Amount: ${:.2f}".format(total_rental_amount))
            invoice_file.write("\n"+"-" * 64)
            invoice_file.write("\n"+"                    Kindly check your Bill"                       )
            invoice_file.write("\n"+"      We hope to serve you again at Birag Equipment Store!!!     ")
            invoice_file.write("\n"+"_________________________________________________________________"+"\n"+"\n")
            invoice_file.write("======================================================================\n")
