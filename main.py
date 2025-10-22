# main.py

from shift_manager import ShiftManager
#from report import generate_shift_report, generate_employee_report,generate_shift_report
import constants
from report import Report
def initialize_data(manager: ShiftManager):
    """Pre-populates the system with initial data."""
    print("\n--- Initializing System Data ---")
    
    # Add Employees
    # manager.add_employee(101, "Alice Smith", "Technician")
    # manager.add_employee(102, "Bob Johnson", "Supervisor")
    # manager.add_employee(103, "Charlie Brown", "Specialist")
    # manager.add_employee(104, "Dana White", "Technician")
    # manager.add_employee(105, "Eve Davis", "Technician")
    
    # Add Shifts
    # manager.add_shift("Morning", 2) # Capacity of 2
    # manager.add_shift("Evening", 3) # Capacity of 3
    # manager.add_shift("Night", 1)   # Capacity of 1
    
    # Initial Assignments
    # manager.assign_employee_to_shift(101, "Morning")
    # manager.assign_employee_to_shift(102, "Evening")
    # manager.assign_employee_to_shift(103, "Evening")
    print("--- Initialization Complete ---")

def display_menu():
    """Displays the main menu options."""
    print("\n" + "~"*40)
    print("  EMPLOYEE & SHIFT MANAGEMENT SYSTEM")
    print("~"*40)
    print("1. Add New Employee")
    print("2. Add New Shift")
    print("3. Assign Employee to Shift")
    print("4. Remove Employee from Shift")
    print("5. Generate Shift Coverage Report")
    print("6. Generate Employee Shift Report")
    print("7. Generate Shift Report")
    print("8. Generate Employee Shedule Report")
    print("9. Exit")
    print("~"*40)


def main():
    manager = ShiftManager()
    initialize_data(manager)
    report = Report()
    while True:
        print("#"*80," - START")

        display_menu()
        choice = input("Enter your choice (1-9): ")

        try:
            if choice == '1':
                employee_id = int(input("Enter Employee ID (integer): "))
                name = input("Enter Employee Name: ")
                role = input(f"Enter Employee Role (e.g., {constants.ROLES_ALLOWED}): ")
                manager.add_employee(employee_id, name, role)
                
            elif choice == '2':
                name = input(f"Enter Shift Name (e.g., {constants.ALLOWED_SHIFTS}): ")
                capacity = int(input("Enter Shift Capacity (integer): "))
                manager.add_shift(name, capacity)

            elif choice == '3':
                employee_id = int(input("Enter Employee ID to assign: "))
                shift_name = input(f"Enter Shift Name : {constants.ALLOWED_SHIFTS} to assign to: ")
                manager.assign_employee_to_shift(employee_id, shift_name)

            elif choice == '4':
                employee_id = int(input("Enter Employee ID to remove: "))
                shift_name = input(f"Enter Shift Name to remove from (ex: {constants.ALLOWED_SHIFTS}): ")
                manager.remove_employee_from_shift(employee_id, shift_name)
            
            elif choice == '5':
                report.shift_summary(manager)

            elif choice == '6':
                report.generate_employee_report(manager)
            elif choice == '7':
                report.generate_shift_report(manager)
            elif choice == '8':
                employee_id = int(input("Enter Employee ID to Get Schedule: "))
                manager.get_employee_schedule(employee_id)
            elif choice == '9':
                print("Exiting System. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")

        except ValueError:
            print("❌ Invalid input. Please ensure you enter the correct data type (e.g., integer for ID/Capacity).")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        print("#"*80," - END")
if __name__ == "__main__":
    main()