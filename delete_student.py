from students import students


def delete_student(name):
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print(f"Student {name} deleted.")
            return True
    print(f"Student {name} not found.")
    return False
