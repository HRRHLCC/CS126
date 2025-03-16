data_dict = {}

with open("Lab8-data.txt", 'r') as file:
    for idx, line in enumerate(file):
        parts = line.strip().split("|")
        data_dict[idx] = tuple(parts)

def sort_data(data_dict):
    sorted_list = sorted(data_dict.values(), key=lambda x: int(x[2]))
    return sorted_list

def display_data(sorted_list):
    print("sorted by age")
    print(f"{'First Name':<12}{'Last Name':<12}{'Age':<6}{'Occupation':<15}")
    print("-" * 45)
    for entry in sorted_list:
        print(f"{entry[0]:<12}{entry[1]:<12}{entry[2]:<6}{entry[3]:<15}")

sorted_list = sort_data(data_dict)
display_data(sorted_list)