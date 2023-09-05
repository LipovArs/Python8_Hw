import csv

class Candidate:
    def __init__(self, first_name, last_name, email, tech_stack, main_skill, main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"Full Name: {self.full_name}\nEmail: {self.email}\nTech Stack: {', '.join(self.tech_stack)}\nMain Skill: {self.main_skill}\nMain Skill Grade: {self.main_skill_grade}"

    @classmethod
    def generate_candidates(cls, file_path):
        candidates = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                if len(data) == 6:
                    first_name, last_name, email, tech_stack_str, main_skill, main_skill_grade = data
                    tech_stack = tech_stack_str.split(';')
                    candidate = cls(first_name, last_name, email, tech_stack, main_skill, main_skill_grade)
                    candidates.append(candidate)

        # Вивести кандидатів на екран
        for candidate in candidates:
            print(candidate)

        return candidates

# Виклик методу для зчитування та виведення кандидатів з файлу
Candidate.generate_candidates('candidates.csv')
