from students import students


def show_students():
    if not students:
        print("No students found.")
        return
    print("--- Students List ---")
    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['name']} | Age: {s['age']} | Group: {s['group']}")

if __name__ == "__main__":
    show_students()
