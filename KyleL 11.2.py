# Employee class Personal information
class Employee:
    def __init__(self, employee_name, employee_number):
        self.employee_name = employee_name
        self.employee_number = employee_number

    def set_employee_name(self, employee_name):
        self.employee_name = employee_name

    def set_employee_number(self, employee_number):
        self.employee_number = employee_number

    def get_employee_name(self):
        return self.employee_name

    def get_employee_number(self):
        return self.employee_number

# Production class for additional information about work
class ProductionWorker(Employee):
    def __init__(self, shift, pay):
        self.shift = shift
        self.pay = pay

    def set_shift(self, shift):
        self.shift = shift

    def set_pay(self, pay):
        self.pay = pay

    def get_shift(self):
        return self.shift

    def get_pay(self):
        return self.pay

# Main class because we are still working in c++ and java
def main():
    # inputs for use with Bob, i mean, any name works, i just went with bob
    name = input("Please enter employees name: ")
    number = int(input("Please enter employee number: "))
    pay = float(input("Please enter pay for employee: "))
    shift = int(input("Please enter employee's shift, 1 for day, 2 for night: "))
    bob = ProductionWorker(shift, pay)
    bob.set_employee_name(name)
    bob.set_employee_number(number)
    # outputs for the user
    print("Worker bob information")
    print("Worker name", bob.get_employee_name())
    print("Worker employee number", bob.get_employee_number())
    print("Worker pay rate", bob.get_pay())
    if bob.get_shift() == 1:
        print("Worker", bob.get_employee_name(),"shift is daytime", "\n")
    elif bob.get_shift() == 2:
        print("Worker",bob.get_employee_name(), "shift is nighttime", "\n")



main()
