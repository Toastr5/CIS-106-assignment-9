class Employee:
  
  def __init__(self, first, last, pay, rate):
    self.first = first
    self.last = last
    self.pay = pay
    self.rate = rate
    self.email = first + '.' + last + '@company.com'
  def fullname(self):
    return ' {} {} '.format(self.first, self.last)
  def bonus(self):
    bonus  = self.rate * self.pay
    return bonus
   

emp_1 = Employee('Corey', 'Schafer', 50000, .10)
emp_2 = Employee('Test', 'User', 60000, .05)

print(f"{emp_1.fullname()} \nBonus: ${emp_1.bonus()}\n")
print(f"{emp_2.fullname()} \nBonus: ${emp_2.bonus()}\n")
