n = int(input())
student_marks = {}
for _ in range(n):
  name, *line = input().split()
  scores = list(map(float, line))
  student_marks[name] = scores
query_name = input()
marks = student_marks[query_name]
total = 0
for _ in range(len(marks)):
  total += marks[_]
print("{:.2f}".format(total/len(marks)))