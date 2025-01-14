class Person:
  def __init__(self, name, age, gender, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.name = name
    self.age = age
    self.gender = gender
  def __init__(self):
    self.name = "Jane Doe"
    self.age = 30
    self.gender = "female"
  def get_goal():
    print("My goal is: Live for the moment!")
  def introduce(self):
    print(f"Hi, I'm {self.name}, a {self.age} year old {self.gender}.")
    
class Student(Person):
  def __init__(self, name, age, gender, previous_organization):
    super.__init__(name = name, age = age, gender = gender)
    self.previous_organization = previous_organization
    self.skipped_days = 0
  def __init__(self):
    super().__init__(self, name = "Jane Doe", age = 30, gender = "female")
    self.previous_organization = "The School of Life"
    self.skipped_days = 0
  def get_goal():
    print("Be a junior software developer.")
  def introduce(self):
    print(f"Hi, I'm {self.name}, a {self.age} year old {self.gender} from {self.previous_organization} who skipped {self.skipped_days} days from the course already.")
  def skip_days(self, number_of_days):
    self.skip_days += number_of_days

class Mentor:
  def __init__(self, name, age, gender, level):
    super().__init__(self, name = name, age = age, gender = gender)
    self.level = level
  def __init__(self):
    super.__init__(name = "Jane Doe", age = 30, gender = "female")
    self.level = "intermidiate"
  def get_goal():
    print("Educate brilliant junior software developers.")
  def introduce(self):
    print(f"Hi, I'm {self.name}, a {self.age} year old {self.gender} {self.level} mentor.")

if __name__ == "__main__":
  student = Student()
  mentor = Mentor()
  person = Person()
  person.get_goal()
  person.introduce()
  student.get_goal()
  student.introduce()
  mentor.get_goal()
  mentor.introduce()