print("continue")
for i in range(10):
    if i == 5:
        continue
    print(i)

print("break")
for i in range(5):
    if i == 3:
        break
    print(i)

print("pass")
for i in range(2):
    pass
print("Pass will not print anything")