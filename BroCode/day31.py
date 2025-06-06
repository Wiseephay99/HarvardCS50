import datetime
print()


class Employee:
    raise_amount = 1.04  # class variables
    num_of_employees = 0  # class variables

    def __init__(self, first, last, salary):
        # Instance variables
        self.first = first
        self.last = last
        # self.email = f'{first}.{last}@email.com'
        self.salary = salary

        Employee.num_of_employees += 1

    ############################################################
    ############################################################
    # PROPERTY DECORATORS GETTERS, SETTERS DELETERS
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    # setter
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    ############################################################
    ############################################################
    # regular methods
    # def full_name(self):
    #     return f'{self.first} {self.last}'

    def __str__(self):
        return f'{self.full_name()} - {self.email}'

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
        # self.salary = int(self.salary * self.raise_amount)

    ############################################################
    ############################################################

    # class methods /constructors
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    ############################################################
    ############################################################

    # STATIC METHODS
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        # return super().__reduce__()
        return f"Employee({self.first} {self.last} {self.salary})"

    def __str__(self):
        # return super().__str__()
        return f'{self.full_name} - {self.email}'

    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.full_name)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('User', 'Test', 600000)

print(emp_1.full_name)
print(emp_2.full_name)

#   alternative
#   print(Employee.full_name(emp_1))
print(emp_1.salary)
emp_1.apply_raise()
print(emp_1.salary)

# acessing the raise amount
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()
print(emp_1.__dict__)

# Employee.raise_amount = 1.05
# emp_1.raise_amount = 2
# emp_2.raise_amount = 3

# kEEPING TRACK OF NUMBER OF EMPLOYEES

print(Employee.num_of_employees)
print()
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print('***************************************************')
# regular methods /class methods /static methods (Constructors)
Employee.set_raise_amt(1.05)
emp_1.set_raise_amt(1.05)
emp_2.set_raise_amt(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print('***************************************************')
print()
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')
emp_3 = Employee(first, last, pay)

print(emp_3.email)
print(emp_3.salary)
# use a;ternative constructor
emp_4 = Employee.from_string(emp_str_2)
emp_5 = Employee.from_string(emp_str_3)

print('***************************************************')
my_date = datetime.date(2025, 4, 16)
print(Employee.is_workday(my_date))

print('***************************************************')
#   Inheritance
# creating developers and managers


class Developer(Employee):
    # raise_amount = 1.10
    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.full_name)


dev_1 = Developer('Wise', 'Ephay', 200000, 'Python')
dev_2 = Developer('Tester', 'Devsek', 100000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang)
print(dev_2.email)
print(dev_2.prog_lang)

print()
# print(help(Developer))
print(dev_1.salary)
dev_1.apply_raise()
print(dev_1.salary)
print('***************************************************')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
mgr_1.remove_emp(dev_2)
mgr_1.print_emps()
print('***************************************************')
# is intance and is substance
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
print('***************************************************')
# Special and Magic /Dunder methods
print(1+2)
print('a' + "b")
print(emp_1)
print('***************************************************')

print(repr(emp_1))
print(str(emp_1))
print(emp_1)
print('***************************************************')

print()
print(1+2)
print(int.__add__(1, 2))
print(int.__add__(1, 2))
print(emp_1 + emp_2)

print(len('test'))

print('test'.__len__())
print('***************************************************')


print(len(emp_1))
print('***************************************************')
# Property Decorators / Getters / Setters and deleters


print('***************************************************')

emp_1 = Employee('Corey', 'Schafer', 50000)

print(emp_1.full_name)
