#Import necessary functions from modules
import return_equipment
import rent_equipment
import display

#Defines main unctions which controls the flow of program
def main():

    # Load equipment data from the file using read_equipment_data function from the display module
    equipment_data = display.read_equipment_data("equipment.txt")

    while True:
        print('''\n
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            |   Welcome To Birag Equipment Store   |
            ----------------------------------------
            |      1: Display Equipment            |   
            |      2: Rent Equipment               |   
            |      3: Return Equipment             |
            |      4: Exit                         |  
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ''')

        try:
            # Prompt the user to select an option
            selectOptions = int(input("Enter an option from 1 to 4: "))

            # Based on the user's choice, perform the corresponding action
            if selectOptions == 1:
                # Call the display_equipment function from the display module to show available equipment
                display.display_equipment(equipment_data)

            elif selectOptions == 2:
                # Call the rent_equipment function from the rent_equipment module to rent equipment
                rent_equipment.rent_equipment(equipment_data)

            elif selectOptions == 3:
                # Call the return_equipment function from the return_equipment module to return equipment
                return_equipment.return_equipment(equipment_data)

            elif selectOptions == 4:
                print("\n"+"     Exiting the program !!! Thank You for visiting our store.     "+"\n")
                break   # Exit the loop and end the program

            else:
                print("----------->>> Please make a valid choice! <<<-----------")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Check if this script is being run directly
if __name__ == "__main__":
    main()  # Call the main function to start the program
