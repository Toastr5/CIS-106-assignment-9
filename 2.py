
class Student:
  def __init__(self,first,last,district,credits):
    self.first = first
    self.last = last
    self.district = district
    self.credits = credits

  def tuition(self):
    if self.district == 'I':
      tuition = self.credits * 250
    else:
      tuition = self.credits * 500
    return tuition

stu_1 = Student('James', 'Evans', 'I', 12)
stu_2 = Student('Lily' , 'Smith', 'O', 10)
stu_3 = Student('Jack', 'Johnson', 'I', 15)

print(stu_1.tuition())
print(stu_2.tuition())
print(stu_3.tuition())