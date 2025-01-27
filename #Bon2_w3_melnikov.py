### Bonus 2
# Write a Python program to filter a list of integers using Lambda.

# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even numbers from the said list:
# [2, 4, 6, 8, 10]

# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: not x%2, original))
odd = list(filter(lambda x: x%2, original))

print(even)
print(odd)