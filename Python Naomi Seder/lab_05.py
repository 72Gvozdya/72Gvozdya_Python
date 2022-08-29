temperatures = []
with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))

print(min(temperatures))
print(max(temperatures))
print(sum(temperatures)/len(temperatures))
temp2 = sorted(temperatures)
print(temp2[len(temperatures)//2])