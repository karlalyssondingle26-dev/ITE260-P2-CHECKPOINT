def average(a, b, c):
    return (a + b + c) / 3


students = int(input("How many students? "))

if students < 3:
    students = 3

for i in range(students):
    print()
    print("Student", i + 1)

    name = input("Enter name: ")
    activity1 = float(input("Activity 1: "))
    activity2 = float(input("Activity 2: "))
    activity3 = float(input("Activity 3: "))

    avg = average(activity1, activity2, activity3)

    if avg >= 90:
        status = "Excellent"
    elif avg >= 80:
        status = "Very Good"
    elif avg >= 75:
        status = "Passed"
    else:
        status = "Failed"

    print()
    print("Name:", name)
    print("Average:", round(avg, 2))
    print("Status:", status)