# yes = []
# for x in range(5):
#     yes.append(x + 1)
# yes = [x for x in range(102) if x % 2 == 0]
student = ["manuel","jaden","julian","aseem","bryson","Barron","noah","dawn"]
# odd = [(student[x])for x in range(len(student)) if len(student[x]) % 2 == 1]
# even = [(student[x])for x in range(len(student)) if len(student[x]) % 2 == 0]
# for x in range(len(student)):
#     if len(student[x])% 2 == 1:
#         odd.append(student[x])
#     if len(student[x]) % 2 == 0:
#         even.append(student[x])
# print(odd)
# print(even)
first = [student[x] for x in range(len(student)) if x < len(student)/2]
last = [student[x] for x in range(len(student)) if x >= len(student)/2]
print(first)
print(last)