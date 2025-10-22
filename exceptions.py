# exceptions.py
import constants
class EmployeeError(Exception):
    """Base exception class for employee and shift management errors."""
    pass

class DoubleBookingError(EmployeeError):
    """Raised when an employee is already assigned to a shift or an overlapping shift."""
    def __init__(self, employee_id, shift_name):
        super().__init__(f"❌ Employee ID {employee_id} is already assigned to a shift.")
        self.employee_id = employee_id
        self.shift_name = shift_name

class ShiftCapacityError(EmployeeError):
    """Raised when trying to assign an employee to a full shift."""
    def __init__(self, shift_name):
        super().__init__(f"❌ Shift '{shift_name}' is already at full capacity.")
        self.shift_name = shift_name

class EmployeeNotFoundError(EmployeeError):
    """Raised when an employee ID is not found."""
    def __init__(self, employee_id):
        super().__init__(f"❌ Employee with ID {employee_id} not found.")
        self.employee_id = employee_id

class ShiftNotFoundError(EmployeeError):
    """Raised when a shift name is not found."""
    def __init__(self, shift_name):
        super().__init__(f"❌ Shift '{shift_name}' not found, allowed shift names are {constants.ALLOWED_SHIFTS}")
        self.shift_name = shift_name

class ShiftNotInitializedError(EmployeeError):
    """Raised when a shift is not initialized or shift not found."""
    def __init__(self, shift_name):
        super().__init__(f"❌ Shift '{shift_name}' is not initialized or shift not found.")
        self.shift_name = shift_name        

class RoleNotFoundError(EmployeeError):
    """Raised when a role name is not found."""
    def __init__(self, role_name):
        super().__init__(f"❌ Role '{role_name}' not found, allowed roles are {constants.ROLES_ALLOWED}.")
        self.role_name = role_name

class ShiftCapacityError(EmployeeError):
    """Raised when a shift capacity exceeded."""
    def __init__(self, shift_capacity):
        super().__init__(f"❌ Shift Capacity '{shift_capacity}' exceeded, max allowed capacity is {constants.MAX_EMPLOYEED_IN_SHIFT}.")
        self.shift_capacity = shift_capacity




