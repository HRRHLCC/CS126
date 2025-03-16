profession_data = {}

with open('lab2-data.txt', 'r') as file:
    next(file)
    for line in file:
        parts = line.strip().split('|')
        if len(parts) >= 5:
            profession = parts[3].strip()
            rate = float(parts[4].strip())
            if profession not in profession_data:
                profession_data[profession] = {'count': 0, 'total_rate': 0.0}
            profession_data[profession]['count'] += 1
            profession_data[profession]['total_rate'] += rate

for profession in sorted(profession_data.keys()):
    total = profession_data[profession]['total_rate']
    count = profession_data[profession]['count']
    average = total / count
    print(f"{profession}: ${average:.2f}")