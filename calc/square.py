numbers = [5,6,32,56,73,52,-3]
s_sum = 0
l_sum = 0

for i in range(0, len(numbers), 2):
    s_sum = s_sum + numbers[i]

for a in range(1, len(numbers), 2):
    a2 = numbers[a] * numbers[a]
    l_sum = l_sum + a2

print(s_sum)
print(l_sum)
