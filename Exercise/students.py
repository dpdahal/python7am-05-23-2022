students = [
    {"name": "Rajesh", "gender": "male", "status": True},
    {"name": "Ram", "gender": "male", "status": False},
    {"name": "Laxmi", "gender": "female", "status": True},
    {"name": "Sophia", "gender": "female", "status": False},
    {"name": "Nandira", "gender": "female", "status": False},
    {"name": "Kopila", "gender": "female", "status": True},
    {"name": "Madan", "gender": "male", "status": True},
]

"""
Total:users?
Total male:?
total female:?
Total active students?
total inactive students?
total active male?
total inactive male?
"""

total_students = len(students)
total_male = 0
total_female = 0
total_active = 0
total_inactive = 0
total_ac_male = 0
total_ac_female = 0

for student in students:
    if student['gender'] == 'male':
        if student['status'] == True:
            total_ac_male += 1
        total_male += 1

    if student['gender'] == 'female':
        if student['status'] == True:
            total_ac_female += 1

        total_female += 1

    if student['status'] == True:
        total_active += 1

    else:
        total_inactive += 1


print(f"Total: {total_students} Total male : {total_male}")