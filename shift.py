# shift.py

from employee import Employee
from exceptions import ShiftCapacityError,ShiftNotFoundError,ShiftCapacityError
import constants

class Shift:

    """
    Represents a work shift (morning/evening/night).

    Attributes:
        shift_name (str): Name of the shift.
        capacity (int): Maximum number of employees allowed.
        employees (list): Employees assigned to this shift.
    """
    def __init__(self, name: str, capacity: int):
        if capacity <= 0:
            raise ValueError("Shift capacity must be positive.")
        if capacity > constants.MAX_EMPLOYEED_IN_SHIFT:
            raise ShiftCapacityError(capacity)
        if name not in constants.ALLOWED_SHIFTS:
            raise ShiftNotFoundError({name})
        
        self.name = name
        self.capacity = capacity
        self.employees = [] # List of Employee objects assigned to this shift
        
        # Define shift times for conflict checking (in a real system, this would be datetime objects)
        # Using simple strings to represent unique, non-overlapping periods for this project
        self.time_slot = name.upper() # 'MORNING', 'EVENING', 'NIGHT'

    def assign_employee(self, employee: Employee):
        """
        Assigns an employee to the shift.
        HINT: Check if capacity is not exceeded before assigning.
        """
        if len(self.employees) >= self.capacity:
            raise ShiftCapacityError(f"Shift '{self.name}' is at full capacity ({self.capacity}).")

        if employee not in self.employees:
            self.employees.append(employee)
            employee.assigned_shifts.add(self.name) # Track the shift name on the employee
            return True
        return False # Employee already assigned to this shift

    def remove_employee(self, employee: Employee):
        """Removes an employee from the shift."""
        if employee in self.employees:
            self.employees.remove(employee)
            employee.assigned_shifts.discard(self.name) # Remove the shift name from the employee
            return True
        return False

    def get_coverage(self):
        """Returns the current number of employees and the total capacity."""
        return len(self.employees), self.capacity
    
    def get_Shifts(self):
        """Provides a readable representation."""
        return (f"Shift(Name='{self.name}', Capacity={self.capacity})")
    
        