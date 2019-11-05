# by Allison Dixon
# last updated November 5, 2019
# unit 6 assignment 1

import random


def are_duplicates(nums):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] == nums[y]:
                return True
    return False


num_runs = int(input("How many times do you want to run the simulation?"))
duplicate_birthday = 0
for x in range(num_runs):
    birthdays = []
    for x in range(23):
        ran = random.randint(1, 365)
        birthdays.append(ran)
    print(are_duplicates(birthdays))
    if are_duplicates(birthdays) is True:
        duplicate_birthday += 1
print((duplicate_birthday/num_runs) * 100)
print("There were", duplicate_birthday, "sets duplicate birthdays.")
