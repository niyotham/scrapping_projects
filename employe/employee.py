
class Employee:
    """ An employee class"""
    def __init__(self, first, last, pay) :
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return f'{self.first}.{self.last}'
    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'
    
    def __repr__(self) -> str:
        return f"Employee('{self.first}','{self.last}','{self.pay}')"

# employee = Employee('niyo', 'thamar', 10.000)
# print(employee.fullname)
# print(employee.email)