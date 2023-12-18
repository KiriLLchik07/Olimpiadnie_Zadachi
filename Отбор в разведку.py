array1 = [0, 0, 0, 1]
f = int(open('input.txt').readline())
for i in range(4, f + 1):
    array1.append(array[(i + 1) // 2] + array1[i // 2])
print(array1[f])
