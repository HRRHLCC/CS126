age_count = {}

with open('lab2-data.txt', 'r') as file:
    next(file)
    for line in file:
        parts = line.strip().split('|')
        if len(parts) >= 3:
            age = int(parts[2].strip())
            age_count[age] = age_count.get(age, 0) + 1

for age in sorted(age_count.keys()):
    print(f"Age: {age} -> Count: {age_count[age]}")