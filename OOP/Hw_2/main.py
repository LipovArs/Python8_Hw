class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f'I come to the ofice {self.work_str}\n'

    def compare(self, sec_empl):
        if self.salary > sec_empl.salary:
            return f"{self.name} has a higher ({self.salary}) salary than {sec_empl.name} ({sec_empl.salary})"
        elif self.salary < sec_empl.salary:
            return f"{self.name} has a lower ({self.salary}) salary than {sec_empl.name} ({sec_empl.salary})"
        else:
            return f"{self.name} has a same ({self.salary}) salary as {sec_empl.name} ({sec_empl.salary})"

    def __str__(self):
        return f"Position: {type(self).__name__}\nName: {self.name}\nSalary: {self.salary}\n"


class Developer(Employee):
    work_str = 'and start to coding'


class Recruiter(Employee):
    work_str = 'and start to hiring'


rec1 = Recruiter("Robert", 100)
dev1 = Developer("Bob", 300)
rec2 = Recruiter("Fill", 200)
dev2 = Developer("Paul", 400)

print(rec1.__str__())
print(dev1.__str__())

print(rec2.work())
print(dev2.work())

print(rec1.compare(dev1))
