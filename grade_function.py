def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "F"


mark = int(input("Enter your mark: "))

grade = calculate_grade(mark)

print("Grade:", grade)