N = int(input())
student_info = []

for _ in range(N):
    name, score = input().split()
    student_info.append((int(score), name))
    
student_info.sort()

for student in student_info:
    print(student[1], end = ' ')
