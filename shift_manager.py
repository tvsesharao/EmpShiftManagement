# shift_manager.py

from employee import Employee
from shift import Shift
from exceptions import DoubleBookingError, EmployeeNotFoundError, ShiftNotFoundError,ShiftCapacityError,ShiftNotInitializedError
import constants

class ShiftManager:
    """
    Manages all shifts and employee assignments.
    """
    def __init__(self):
        self.employees = {}  # {employee_id: Employee_object}
        self.shifts = {}     # {shift_name: Shift_object}
        
    # --- Employee Management ---
    
    def add_employee(self, employee_id: int, name: str, role: str):
        """
        Add an employee to the system.
        """
        if employee_id in self.employees:
            print(f" Error: Employee with ID {employee_id} already exists.")
            return False
        
        try:
            employee = Employee(employee_id, name, role)
            self.employees[employee_id] = employee
            print(f"✅ Employee added: {employee}")
            return True
        except ValueError as e:
            print(f"❌ Error adding employee: {e}")
            return False
            
    def get_employee(self, employee_id: int) -> Employee:
        """Retrieves an employee by ID."""
        employee = self.employees.get(employee_id)
        if not employee:
            raise EmployeeNotFoundError(f"Employee with ID {employee_id} not found.")
        return employee

    # --- Shift Management ---

    def add_shift(self, name: str, capacity: int):
        """
        Create a new shift with given name and capacity.
        """
        if name not in constants.ALLOWED_SHIFTS:
            raise ShiftNotFoundError(name)	
        if name in self.shifts:
            print(f"❌ Error: Shift '{name}' already exists.")
            return False
        if capacity > constants.MAX_EMPLOYEED_IN_SHIFT:
            raise ShiftCapacityError(capacity)
        try:
            shift = Shift(name, capacity)
            self.shifts[name] = shift
            print(f"✅ Shift added: {shift}")
            return True
        except ValueError as e:
            print(f"❌ Error adding shift: {e}")
            return False

    def get_shift(self, shift_name: str) -> Shift:
        """Retrieves a shift by name."""
        shift = self.shifts.get(shift_name)
        if not shift:
            raise ShiftNotInitializedError(shift_name)
        return shift
        
    # --- Assignment Logic ---

    def assign_employee_to_shift(self, employee_id: int, shift_name: str):
        """
        Assigns employee to a shift.
        HINT: Prevent double-booking (employee already in another shift).
        HINT: Raise errors from exceptions.py if invalid.
        """
        try:
            if shift_name not in constants.ALLOWED_SHIFTS:
                raise ShiftNotFoundError(shift_name)
            employee = self.get_employee(employee_id)
            shift = self.get_shift(shift_name)
            
            # 1. Prevent Double-Booking (Overlapping Shifts)
            # In this simple model, we assume all defined shifts (Morning/Evening/Night) 
            # represent non-overlapping time slots on the same day. 
            # Therefore, an employee can only be assigned to one shift per day (or cycle).
            if employee.assigned_shifts:
                raise DoubleBookingError(
                    f"⚠️Employee {employee.name} (ID {employee_id}) is already assigned to a shift: {list(employee.assigned_shifts)}. "
                    "Cannot assign to another shift in the same cycle."
                )

            # 2. Assign and Check Capacity
            if shift.assign_employee(employee):
                print(f"✅ Successfully assigned {employee.name} to shift '{shift.name}'.")
            else:
                # Should not happen if capacity check is correct, but handles re-assignment attempts
                print(f"⚠️ Employee {employee.name} was already in shift '{shift.name}'.")

        except (EmployeeNotFoundError, ShiftNotFoundError, DoubleBookingError, ShiftCapacityError) as e:
            print(f"❌ Assignment failed: {e}")
            
    def remove_employee_from_shift(self, employee_id: int, shift_name: str):
        """Removes an employee from a shift."""
        try:
            if shift_name not in constants.ALLOWED_SHIFTS:
                raise ShiftNotFoundError(shift_name)
            employee = self.get_employee(employee_id)
            shift = self.get_shift(shift_name)
            
            if shift.remove_employee(employee):
                print(f"✅ Successfully removed {employee.name} from shift '{shift.name}'.")
            else:
                print(f"⚠️ Employee {employee.name} was not assigned to shift '{shift.name}'.")

        except (EmployeeNotFoundError, ShiftNotFoundError) as e:
            print(f"❌ Removal failed: {e}")
    def get_employee_schedule(self, emp_id):
        """
        Return the shift(s) that the employee is assigned to.
        """
        employee = self.get_employee(emp_id)
        if employee.assigned_shifts:
            print(list(employee.assigned_shifts))
            