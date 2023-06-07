import csv

# numbers = [1,1,2,3,4,5,7,9,12]
#
# squared_numbers = [number * number for number in numbers]
#
# result = [number for number in squared_numbers if number % 2 == 0]
#
# print(result)
with open('file1.txt') as file1:
    numbers_file1 = file1.readlines()
    print(numbers_file1)

with open('file2.txt') as file2:
    numbers_file2 = file2.readlines()

# numbers_file2 = pandas.read_csv('file2.txt')

common_numbers_list = [int(number) for number in numbers_file1 if number in numbers_file2]

print(common_numbers_list)