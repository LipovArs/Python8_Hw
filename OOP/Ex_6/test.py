import unittest
from your_module import Employee, Developer, Recruiter, Candidate

class TestEmployee(unittest.TestCase):
    def test_employee_creation(self):
        employee = Employee("John", 1000, "john@example.com")
        self.assertEqual(employee.name, "John")
        self.assertEqual(employee.salary, 1000)
        self.assertEqual(employee.email, "john@example.com")


class TestDeveloper(unittest.TestCase):
    def test_developer_creation(self):
        developer = Developer("Alice", 2000, "alice@example.com", ["Python", "Java"])
        self.assertEqual(developer.name, "Alice")
        self.assertEqual(developer.salary, 2000)
        self.assertEqual(developer.email, "alice@example.com")
        self.assertEqual(developer.tech_stack, ["Python", "Java"])


class TestRecruiter(unittest.TestCase):
    def test_recruiter_creation(self):
        recruiter = Recruiter("Bob", 1500, "bob@example.com")
        self.assertEqual(recruiter.name, "Bob")
        self.assertEqual(recruiter.salary, 1500)
        self.assertEqual(recruiter.email, "bob@example.com")


class TestCandidate(unittest.TestCase):
    def test_candidate_creation(self):
        candidate = Candidate("Eva", "Smith", "eva@example.com", ["Python", "JavaScript"], "Python", "Junior")
        self.assertEqual(candidate.first_name, "Eva")
        self.assertEqual(candidate.last_name, "Smith")
        self.assertEqual(candidate.email, "eva@example.com")
        self.assertEqual(candidate.tech_stack, ["Python", "JavaScript"])
        self.assertEqual(candidate.main_skill, "Python")
        self.assertEqual(candidate.main_skill_grade, "Junior")


if __name__ == '__main__':
    unittest.main()
