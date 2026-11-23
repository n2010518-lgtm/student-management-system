from students import students, add_student


def main():
    print("=== Student Management System ===")
    add_student("Askat", 20, "CS-101")
    print(f"Total students: {len(students)}")


if __name__ == "__main__":
    main()
