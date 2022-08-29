with open('r1.txt', 'r') as f, open('result.txt', 'w') as result:
    for line in f:
        if line.startswith("service"):
            result.write(line)