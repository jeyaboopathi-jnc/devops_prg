def calculate_total(m1, m2, m3):
    return m1 + m2 - m3

def calculate_average(total):
    return total / 3

total = calculate_total(85, 90, 80)
average = calculate_average(total)

print("Total Marks:", total)
print("Average Marks:", average)
