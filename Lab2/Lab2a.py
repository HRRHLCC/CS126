data_list = []

with open("Lab2-data.txt","r") as data:
    next(data)
    for line in data:
            parts = line.strip().split('|')
            if len(parts) >= 3:
                name = parts[1].strip()
                age = int(parts[2].strip())
                data_list.append(f"{age}|{name}")
    data_list.sort(key=lambda x: (int(x.split('|')[0]), x.split('|')[1]))
for entry in data_list:
    age, name = entry.split('|')
    print(f"{age}:{name}")