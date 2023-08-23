import datetime

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f'I come to the ofice {self.work_str}\n'

    def compare(self, sec_empl):
        if self.salary > sec_empl.salary:
            return f"{self.name} has a higher ({self.salary}) salary than {sec_empl.name} ({sec_empl.salary})\n"
        elif self.salary < sec_empl.salary:
            return f"{self.name} has a lower ({self.salary}) salary than {sec_empl.name} ({sec_empl.salary})\n"
        else:
            return f"{self.name} has a same ({self.salary}) salary as {sec_empl.name} ({sec_empl.salary})\n"

    def __str__(self):
        return f"Position: {type(self).__name__}\nName: {self.name}\nSalary: {self.salary}\n"

    def  check_salary(self, days):
      today = datetime.date.today()
      start_of_month = today.replace(day=1)
      days_worked = 0

      current_day = start_of_month
      while current_day <= today:
        if current_day.weekday() < 5:
          days_worked += 1
        current_day += datetime.timedelta(days=1)

      return f"{self.name} have {self.salary * days} salary for {days} days\nAnd {self.salary * days_worked} from start of month\n"
      

class Developer(Employee):
  work_str = 'and start to coding'
  
  def __init__(self, name, salary, tech_stack):
    super().__init__(name, salary)
    self.tech_stack = tech_stack

  def __str__(self):
        return f"Position: {type(self).__name__}\nName: {self.name}\nSalary: {self.salary}\nStack: {self.tech_stack}"
    
  def compare_stack_sum(self, sec_dev):
      
      if len(self.tech_stack) > len(sec_dev.tech_stack):
          return f"{self.name} has a higher ({len(self.tech_stack)}) stack than {sec_dev.name} ({len(sec_dev.tech_stack)})\n"
      elif len(self.tech_stack) < sec_dev.salary:
          return f"{self.name} has a lower ({len(self.tech_stack)}) stack than {sec_dev.name} ({len(sec_dev.tech_stack)})\n"
      else:
          return f"{self.name} has a same ({len(self.tech_stack)}) stack as {sec_dev.name} ({len(sec_dev.tech_stack)})\n"

  def __add__(self, sec_dev):
    new_name = f'{self.name} {sec_dev.name}'
    stack_sum = list(set(self.tech_stack + sec_dev.tech_stack))
    salar = max(self.salary, sec_dev.salary)

    return Developer(new_name, salar, stack_sum)

class Recruiter(Employee):
    work_str = 'and start to hiring'


rec1 = Recruiter("Robert", 100)
dev1 = Developer("Bob", 300, ["C++", "Java", "Docker", "Git", "Spring", "MySQL"])
rec2 = Recruiter("Fill", 200)
dev2 = Developer("Paul", 400, ["Python", "Django", "Flask", "PSQL", "HTML", "CSS", "JS", "Git", "Docker", "Pandas", "TensorFlow", "NumPy", "PyTorch"])

print(rec1)
print(dev1)

print(rec2.work())
print(dev2.work())

print(rec1.compare(dev1))

print(dev1.check_salary(5))

print(dev1.compare_stack_sum(dev2))

dev3 = dev1 + dev2
print(dev3)