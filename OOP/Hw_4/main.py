import datetime
import csv
import exceptions


class Employee:
    def __init__(self, name, salary, email):
        self.name = name
        self.salary = salary
        self.email = email
        try:
            self.validate()
        except exceptions.EmailAlreadyExistsException as emailException:
            self.log_exception(emailException)
            raise emailException

        self.save_email()

    def work(self):
        return f'I come to the office {self.work_str}\n'

    def compare(self, sec_empl):
        if self.salary > sec_empl.salary:
            return f"{self.name} has a higher ({self.salary}) salary than {sec_empl.name} ({sec_empl.salary})\n"
        elif self.salary < sec_empl.salary:
            return f"{self.name} has a lower ({self.salary}) salary than {sec_empl.name} ({sec_empl.salary})\n"
        else:
            return f"{self.name} has the same ({self.salary}) salary as {sec_empl.name} ({sec_empl.salary})\n"

    def __str__(self):
        return f"Position: {type(self).__name__}\nName: {self.name}\nSalary: {self.salary}\n"

    def check_salary(self, days):
        today = datetime.date.today()
        start_of_month = today.replace(day=1)
        days_worked = 0

        current_day = start_of_month
        while current_day <= today:
            if current_day.weekday() < 5:
                days_worked += 1
            current_day += datetime.timedelta(days=1)

        return f"{self.name} has {self.salary * days} salary for {days} days\nAnd {self.salary * days_worked} from the start of the month\n"

    def save_email(self):
        with open('emails.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.email])

    def validate(self):
        with open('emails.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                _, existing_email = row
                if existing_email == self.email:
                    raise exceptions.EmailAlreadyExistsException("Email already exists")

    def log_exception(self, emailException):
        now = datetime.datetime.now()
        with open('logs.txt', mode='a') as log_file:
            log_file.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')} | Exception occurred: {str(emailException)}\n")
            import traceback
            traceback.print_exc(file=log_file)
            log_file.write("\n")

class Developer(Employee):
    work_str = 'and start to coding'

    def __init__(self, name, salary, email, tech_stack=None):
        super().__init__(name=name, salary=salary, email=email)
        self.tech_stack = tech_stack

    def __str__(self):
        return f"Position: {type(self).__name__}\nName: {self.name}\nSalary: {self.salary}\nStack: {self.tech_stack}"

    def compare_stack_sum(self, sec_dev):
        if len(self.tech_stack) > len(sec_dev.tech_stack):
            return f"{self.name} has a higher ({len(self.tech_stack)}) stack than {sec_dev.name} ({len(sec_dev.tech_stack)})\n"
        elif len(self.tech_stack) < len(sec_dev.tech_stack):
            return f"{self.name} has a lower ({len(self.tech_stack)}) stack than {sec_dev.name} ({len(sec_dev.tech_stack)})\n"
        else:
            return f"{self.name} has the same ({len(self.tech_stack)}) stack as {sec_dev.name} ({len(sec_dev.tech_stack)})\n"

    def __add__(self, sec_dev):
        new_name = f'{self.name} {sec_dev.name}'
        stack_sum = list(set(self.tech_stack + sec_dev.tech_stack))
        salary = max(self.salary, sec_dev.salary)

        return Developer(new_name, salary, stack_sum)

class Recruiter(Employee):
    work_str = 'and start to hiring'

rec1 = Recruiter("Robert", 100, 'robert111@gmail.com')
dev1 = Developer("Bob", 300, 'bob111@gmail.com', ["C++", "Java", "Docker", "Git", "Spring", "MySQL"])
rec2 = Recruiter("Fill", 200, 'fill111@gmail.com')
dev2 = Developer("Paul", 400, 'paul111@gmail.com', ["Python", "Django", "Flask", "PSQL", "HTML", "CSS", "JS", "Git", "Docker", "Pandas", "TensorFlow", "NumPy", "PyTorch"])

print(rec1)
print(dev1)

print(rec2.work())
print(dev2.work())

print(rec1.compare(dev1))

print(dev1.check_salary(5))

print(dev1.compare_stack_sum(dev2))

dev3 = dev1 + dev2
print(dev3)
