# by Allison Dixon
# last updated November 6, 2019
# unit 6 assignment 1

import random


def are_duplicates(nums):
    """
    This function finds duplicate birthdays by comparing the items in a list
    :param nums: the list
    :return: True if there is a duplicate, False if there isn't
    """
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] == nums[y]:
                return True
    return False


def main():
    num_runs = int(input("How many times do you want to run the simulation?"))
    duplicate_birthday = 0
    for x in range(num_runs):
        birthdays = []
        for y in range(23):
            ran = random.randint(1, 365)
            birthdays.append(ran)
        if are_duplicates(birthdays) is True:
            duplicate_birthday += 1
    print("There were duplicate birthdays", (duplicate_birthday/num_runs) * 100, "% of the time.")
    print(duplicate_birthday, "of the simulations run had duplicate birthdays.")


main()
