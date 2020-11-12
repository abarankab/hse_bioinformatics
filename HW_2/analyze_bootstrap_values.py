from statistics import mean, median

values = list(map(int, input().split()))
values.sort()

smallest_size = 5

print(f"Average of {smallest_size} smallest values: {mean(values[:smallest_size])}")
print(f"Average value: {mean(values)}")
print(f"Median value: {median(values)}")