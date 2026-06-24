class Person:
    """Base class for basic personal information"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    """Employee Class (Base Class for work-related data)"""
    def __init__(self, name=None, age=None, employee_id=None, salary=None):
            # Method Overloading handling (Multiple ways of creating objects)
        if name is not None and age is not None and employee_id is None and salary is None:
            # If only name and age are provided (Like a general person)
            super().__init__(name, age)
            self.__employee_id = "Not Assigned"
            self.__salary = 0.0
        else:
            # Standard constructor with all details
            super().__init__(name if name else "Unknown", age if age else 0)
            # Encapsulation: Making attributes private using '__'
            self.__employee_id = employee_id if employee_id else "N/A"
            self.__salary = float(salary) if salary else 0.0

    # Getter and Setter methods for employee_id
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter and Setter methods for salary
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = float(salary)
        else:
            print("Salary cannot be negative!")

    # Method Overriding: Displaying employee details
    def display(self):
        super().display()
        print(f"Employee ID: {self.__employee_id}")
        print(f"Salary: ${self.__salary:.1f}")

    # Destructor to clean up resources
    def __del__(self):
        pass 


class Manager(Employee):
    """Manager Class (Derived Class)"""
    def __init__(self, name, age, employee_id, salary, department):
        # Use of super() to call parent constructor
        super().__init__(name, age, employee_id, salary)
        # Additional Attribute
        self.department = department

    # Method Overriding
    def display(self):
        super().display()
        print(f"Department: {self.department}")


class Developer(Employee):
    """Developer Class (Derived Class)"""
    def __init__(self, name, age, employee_id, salary, programming_language):
        # Use of super() to call parent constructor
        super().__init__(name, age, employee_id, salary)
        # Additional Attribute
        self.programming_language = programming_language

    # Method Overriding
    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")


def main():
    # Lists to store created objects
    persons_list = []
    employees_list = []
    managers_list = []
    developers_list = []

    print("--- Python OOP Project: Employee Management System ---")

    while True:
        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            
            # Using Employee class constructor with name and age (Method Overloading concept)
            person_obj = Employee(name, age)
            persons_list.append(person_obj)
            print(f"\nPerson created with name: {name} and age: {age}.")
            print("--- Choose another operation ---")

        elif choice == 2:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))

            emp_obj = Employee(name, age, emp_id, salary)
            employees_list.append(emp_obj)
            print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary:.1f}.")
            print("--- Choose another operation ---")

        elif choice == 3:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")

            mgr_obj = Manager(name, age, emp_id, salary, dept)
            managers_list.append(mgr_obj)
            print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary:.1f}, and department: {dept}.")
            print("--- Choose another operation ---")

        elif choice == 4:
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            
            try:
                detail_choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice!")
                continue

            if detail_choice == 1:
                if not persons_list:
                    print("No Person records found!")
                else:
                    print("\nPerson Details:")
                    for p in persons_list:
                        # Displaying only Name and Age as required for Person
                        print(f"Name: {p.name}")
                        print(f"Age: {p.age}")
                        print("-" * 20)

            elif detail_choice == 2:
                if not employees_list:
                    print("No Employee records found!")
                else:
                    print("\nEmployee Details:")
                    for e in employees_list:
                        e.display()
                        print("-" * 20)

            elif detail_choice == 3:
                if not managers_list:
                    print("No Manager records found!")
                else:
                    print("\nManager Details:")
                    for m in managers_list:
                        m.display()
                        print("-" * 20)
            else:
                print("Invalid Choice!")
            
            print("--- Choose another operation ---")

        elif choice == 5:
            # Demonstrating issubclass() requirement before exiting
            print("\nChecking Class Hierarchy (issubclass):")
            print(f"Is Manager a subclass of Employee? {issubclass(Manager, Employee)}")
            print(f"Is Developer a subclass of Employee? {issubclass(Developer, Employee)}")
            
            # Explicitly deleting objects to trigger destructor demonstration
            del persons_list, employees_list, managers_list, developers_list
            
            print("\nExiting the system. All resources have been freed.")
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select from 1 to 5.")


if __name__ == "__main__":
    main()
