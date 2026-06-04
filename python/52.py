class Gradebook:
    def __init__(self):
        self.students = {}

    def add_grade(self, student, grade):
        if not isinstance(grade, (int, float)) or grade < 0 or grade > 100:
            print("Invalid grade")
            return
        if student not in self.students:
            self.students[student] = []
        self.students[student].append(grade)

    def calculate_gpa(self, student):
        grades = self.students.get(student, [])
        if not grades: return 0
        return sum(grades) / len(grades)

    def class_average(self):
        all_grades = [g for grades in self.students.values() for g in grades]
        if not all_grades: return 0
        return sum(all_grades) / len(all_grades)

gb = Gradebook()
gb.add_grade("vikram", 85)
gb.add_grade("sankar", 90)
gb.add_grade("navin", 78)
print(f"Vikram GPA: {gb.calculate_gpa('vikram')}")
print(f"Class Average: {gb.class_average()}")
