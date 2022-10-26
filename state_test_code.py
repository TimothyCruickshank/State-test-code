import os 
from statistics import mean, stdev
os.system ('cls')


num = [int(line) for line in open ('Grill_1.txt', 'r')]
min_num, max_num, mean_num, dev_num = min(num), max(num), mean(num), stdev(num)

print(f"Min: {min_num}")
print(f"Max: {max_num}")
print(f"Mean: {mean_num}")
print(f"Standard Deviation of temp is {dev_num}")

