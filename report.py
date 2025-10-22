# report.py

from shift_manager import ShiftManager
from shift import Shift
class Report:
    def __init__(self):
        pass
    """
    Generates reports for employees and shifts.
    """
    def shift_summary(self,manager: ShiftManager):
        """
        Print summary of all shifts and their assigned employees.
        """
        print("\n" + "="*50)
        print("           SHIFT COVERAGE REPORT")
        print("="*50)
        
        if not manager.shifts:
            print("No shifts have been created yet.")
            return

        for name, shift in manager.shifts.items():
            current, capacity = shift.get_coverage()
            coverage = f"{current}/{capacity}"
            status = "FULL" if current == capacity else ("LOW" if current < capacity/2 else "OK")
            
            print(f"\nShift: {name} (Capacity: {capacity}, Status: {status})")
            print("-" * (len(name) + 7))
            
            if shift.employees:
                employee_list = [f" - {emp.name} (ID: {emp.employee_id}, Role: {emp.role})" 
                                for emp in shift.employees]
                print("\n".join(employee_list))
            else:
                print("No employees assigned.")
                
        print("="*50)

    def generate_employee_report(self,manager: ShiftManager):
        """
        Print schedule of a specific employee.
        """
        print("\n" + "="*50)
        print("           EMPLOYEE SHIFT REPORT")
        print("="*50)
        
        if not manager.employees:
            print("No employees have been created yet.")
            return

        for emp_id, employee in manager.employees.items():
            shifts = ", ".join(employee.assigned_shifts) if employee.assigned_shifts else "Unassigned"
            print(f"ID: {emp_id:<5} | Name: {employee.name:<15} | Role: {employee.role:<10} | Shift(s): {shifts}")
            
        print("="*50)

    def generate_shift_report(self, manager: ShiftManager):
        """Generates a report showing Shifts."""
        print("\n" + "="*50)
        print("           SHIFT REPORT")
        print("="*50)
        
        if not manager.shifts:
            print("No shifts have been created yet.")
            return

        for name , shft in manager.shifts.items():
            print(f"Shift Name : {name} | Capacity: {shft.capacity}")
        print("="*50)    

    def generate_employee_schedule(self,manager: ShiftManager):
        """Generates a report showing Shifts."""
        print("\n" + "="*50)
        print("           SHIFT REPORT")
        print("="*50)
        
        if not manager.shifts:
            print("No shifts have been created yet.")
            return

        for name , shft in manager.get_employee_schedule().items():
            print(f"Shift Name : {name} | Capacity: {shft}")
        print("="*50)