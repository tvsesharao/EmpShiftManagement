'''

### `employee.py`
'''
import constants
from exceptions import RoleNotFoundError

class Employee:
    """
    Represents an employee in the organization.

    Attributes:
        emp_id (str): Unique ID for the employee.
        name (str): Employee name.
        role (str): Job role of the employee (e.g., Doctor, Engineer, Cashier).
    """
    def __init__(self, employee_id: int, name: str, role: str):
        if not isinstance(employee_id, int) or employee_id <= 0:
            raise ValueError("Employee ID must be a positive integer.")
        if role not in constants.ROLES_ALLOWED:
            raise RoleNotFoundError(role)
        self.employee_id = employee_id
        self.name = name
        self.role = role
        # Tracks shifts assigned to this employee to easily check for double-booking
        self.assigned_shifts = set()

    def __repr__(self):
        """
        Returns a string like: "E101 - Alice (Nurse)"
        """
        return f"Employee(ID={self.employee_id}, Name='{self.name}', Role='{self.role}')"

    def __hash__(self):
        """Allows Employee objects to be used in sets/dictionaries."""
        return hash(self.employee_id)

    def __eq__(self, other):
        """Compares employees based on their ID."""
        if isinstance(other, Employee):
            return self.employee_id == other.employee_id
        return False