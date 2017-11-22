#!/usr/bin/python3

import datetime

class Employee:

  raise_amount = 1.04
  num_of_employee = 0

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    # self.email = first + '.' + last + '@company.com'
    Employee.num_of_employee += 1
  
  @property
  def email(self):
    '''
    Property decorator
    Note: when using property decorator, make sure that property is not initially by class
    Usage: print(emp_1.email) # instead of function
    '''
    return '{}.{}@email.com'.format(self.first, self.last)

  @property
  def getName(self):
    return '{} {}'.format(self.first, self.last)

  @getName.setter
  def getName(self, name):
    first, last, = name.split(' ')
    self.first = first
    self.last = last

  @getName.deleter
  def getName(self):
    '''
    Usage: del emp_1.getName
    '''
    print('Delete name!')
    self.first = None
    self.last = None

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)

  @classmethod
  def set_raise_amount(cls, amount):
    cls.raise_amount = amount

  @classmethod
  def from_string(cls, emp_str):
    '''Works like an alternative constructor'''
    first, last, pay = emp_str.split('-')
    return cls(first, last, pay)

  @staticmethod
  def is_work_day(day):
    if day.weekday() == 5 or day.weekday() == 6:
      return False
    return True

  def __repr__(self):
    '''
    Dunder methods, used by developer to output object (better representation)
    Usage: print(emp_1.__repr__())
    Example: Employee('Corey', 'Schafer', '50000')
    '''
    return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

  def __str__(self):
    '''
    Dunder methods, for better representation, usually for client display purposes
    Usage: print(emp_1.__str__())
    Example: Corey Schafer - Corey.Schafer@company.com
    '''
    return '{} - {}'.format(self.getName(), self.email)

  def __add__(self, other):
    '''
    return 2 employees salary with the use of dunder method
    Usage: print(dev_1 + dev_2)
    '''
    return self.pay + other.pay


class Developer(Employee):
  raise_amount = 1.10

  def __init__(self, first, last, pay, prog_lang):
    super().__init__(first, last, pay) # calling parent init method, more maintainable
    self.prog_lang = prog_lang

class Manager(Employee):
  def __init__(self, first, last, pay, employees=None):
    super().__init__(first, last, pay)
    if employees is None:
      self.employees = []
    else:
      self.employees = employees

  def add_employee(self, emp):
    if emp not in self.employees:
      self.employees.append(emp)

  def remove_employee(self, emp):
    if emp in self.employees:
      self.employees.remove(emp)

  def print_employee(self):
    for emp in self.employees:
      print('-->', emp.getName())














































emp_1 = Employee('Corey', 'Schafer', 50000)

dev_1 = Developer('Dev', 'Schafer', 50000, 'Python')
dev_2 = Developer('Dev', 'RN', 50000, 'React Native')

manager_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# emp_1_str = 'John-Doe-70000'
# emp_1 = Employee.from_string(emp_1_str)
# print(emp_1.getName())

# today = datetime.date(2017, 11, 23)
# print(Employee.is_work_day(today))


# print(dev_1.getName())
# print(help(Developer))

# print(manager_1.email)
# print(manager_1.print_employee())
# manager_1.add_employee(dev_2)
# print(manager_1.print_employee())

# dunder methods
# print(emp_1)
# print(dev_1 + dev_2)

# property decorator
print(emp_1.email)
print(emp_1.getName)