# Booking.com employee class
from datetime import date

class Employee:
    # class variable
    num_of_employee = 0
    raise_amt = 1.50
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '-' + last + '@email.com'

        Employee.num_of_employee +=1
        
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    # niz-j-1000
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True

class Developer(Employee):
    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.language = language
    def __str__(self):
        return f'name = {self.first} {self.last}' 

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print(emp.fullname())

emp_1 = Employee('Niz', 'J', 1000)
# print(emp_1.first, emp_1.last, emp_1.email)
# print(emp_1.fullname())

# Payment
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print('*'*30)

dev_1 = Developer('Sole', 'S', 10000, 'java')
dev_2 = Developer('Nick', 'N', 10000,'Python')
# print(dev_1)

# print(Employee.raise_amt)
# Employee.set_raise_amt(1.8)
# print(Employee.raise_amt)


# Request

# new_emp_1 =Employee.from_string('Niz-J-1000')
# print(new_emp_1.first)


# new_date = date(2020,9,26)
# print(Employee.is_workday(new_date))
# manager_1 = Manager('Niz', 'J', 90000, [dev_1, dev_2])

# print(manager_1.email)

# manager_1.print_emp()
