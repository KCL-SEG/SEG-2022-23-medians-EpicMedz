"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
numbers.sort()
print(numbers)
if len(numbers) % 2 == 0:
    middle = (len(numbers) / 2) - 1
    middle = int(middle)
    median = (numbers[middle] + numbers[middle + 1]) / 2
    print(median)
else:
    middle = round(len(numbers) / 2)
    median = numbers[middle]
    print(median)
