# Import the datetime module
import datetime

# Import the display_equipment function from the display module
from display import display_equipment

# Function to handle equipment return
def return_equipment(equipment_list):

    # Display the available equipment to the user
    display_equipment(equipment_list)

    try:
        # Get customer's name
        customer_name = input("Enter your name: ")

        # Get the current return date and time
        return_date = datetime.datetime.now()

        # Initialize a variable to keep track of the total return amount
        total_return_amount = 0

        # Initialize a list to store return details for generating invoice
        return_details_list = []

        while True:
            # Get the user's choice for the equipment to return
            choice = int(input("Enter the Equipment Id you are returning (or 0 to finish): ")) - 1

            # Check if the choice is valid or the user wants to finish
            if choice < -1 or choice >= len(equipment_list):
                print("Invalid choice.")
                continue
            elif choice == -1:
                break

            # Get the selected equipment
            equipment = equipment_list[choice]

            # Get the number of days the equipment was rented for, ensuring it's positive
            while True:
                try:
                    rented_days = int(input(f"Enter the number of days you rented {equipment['name']} for: "))
                    if rented_days <= 0:
                        print("Number of days must be a positive value")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number.")

            # Calculate rental periods based on the duration
            rental_duration = 5
            rental_periods = rented_days // 5
            if rented_days % 5 != 0:
                rental_periods += 1

            # Get the price per 5 days from equipment data
            rental_price_per_period = float(equipment["price"].replace("$", ""))

            # Get the quantity of equipment being returned, ensuring it's positive
            while True:
                try:
                    returned_quantity = int(input(f"Enter the quantity of {equipment['name']} you are returning: "))
                    if returned_quantity <= 0:
                        print("Returned quantity must be a positive number.")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number.")

            equipment["quantity"] += returned_quantity

            # Calculate total return amount
            return_amount = rental_price_per_period * rental_periods * returned_quantity

            total_return_amount += return_amount

            return_details_list.append(
                {
                    "equipment_name": equipment["name"],
                    "brand_name": equipment["brand"],
                    "rental_duration": rented_days,
                    "quantity_returned": returned_quantity,
                    "rental_price_per_5_days": equipment["price"],
                    "total_amount": return_amount,
                }
            )

            print(f"\nReturned {returned_quantity} {equipment['name']} that was rented for {rented_days} days.")

        if total_return_amount > 0:
            print("\nEquipment returned successfully!")
            print(f"Total return amount: ${total_return_amount:.2f}")

            # Write updated equipment data to the file
            with open("equipment.txt", "w") as equipment_file:
                for equip in equipment_list:
                    equipment_file.write(
                        f"{equip['name']}, {equip['brand']}, {equip['price']}, {equip['quantity']}\n"
                    )

            # Generate return invoices
            generate_return_invoices(customer_name, return_date, return_details_list, total_return_amount)

        else:
            print("No equipment returned.")

    except ValueError:
        print("Invalid input. Please enter a valid value.")

def generate_return_invoices(customer_name, return_date, return_details_list, total_return_amount):
    invoice_name = f"{customer_name}_{return_date.strftime('%Y-%m-%d_%H-%M-%S')}_return_invoice.txt"
    with open(invoice_name, "w") as invoice_file:
        invoice_file.write("\n"+"________________________________________________________________")
        invoice_file.write("\n"+f"Date: {return_date.strftime('%Y-%m-%d %H:%M:%S')}")
        invoice_file.write("\n"+"____________________    Returned Invoice    ____________________")
        invoice_file.write("\n"+"                                                                ")
        invoice_file.write("\n"+" ******************** Birag Equipment Store ********************")
        invoice_file.write("\n"+"    ---------------------Inaruwa,Nepal----------------------    ")
        invoice_file.write("\n"+"   PAN No. 77777                          Contact No.: 980010200")
        invoice_file.write("\n"+"----------------------------------------------------------------")
        invoice_file.write("\n"+f"Customer Name: {customer_name}")

        for idx, return_details in enumerate(return_details_list, start=1):
            invoice_file.write("\n\n"+"Transaction #" + str(idx) + ":")
            invoice_file.write("\n"+f"Equipment Name: {return_details['equipment_name']}")
            invoice_file.write("\n"+f"Brand Name: {return_details['brand_name']}")
            invoice_file.write("\n"+f"Rental Duration: {return_details['rental_duration']} days")
            invoice_file.write("\n"+f"Quantity Returned: {return_details['quantity_returned']}")
            invoice_file.write("\n"+f"Price per 5 days: {return_details['rental_price_per_5_days']}")
            invoice_file.write("\n"+f"Total Amount: ${return_details['total_amount']:.2f}")
            invoice_file.write("\n"+"-" * 64)

            invoice_file.write("\n\nTotal Return Amount: ${:.2f}".format(total_return_amount))
            invoice_file.write("\n"+"-" * 64)
            invoice_file.write("\n"+"                 Thank you for returning the equipment"           )
            invoice_file.write("\n"+"        We hope to serve you again at Birag Equipment Store!!!")
            invoice_file.write("\n"+"_______________________________________________________"+"\n"+"\n")
            invoice_file.write("======================================================================\n")
