students = []


def add_student(name, age, group):
    student = {"name": name, "age": age, "group": group}
    students.append(student)
    print(f"Student {name} added.")
