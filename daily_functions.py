# created by Allison Dixon
# last updated October 30, 2019
# unit 6 daily functions

# problem 1 prints names from the list in different orders
names = ["Abigail", "Brenda", "Chad", "Doug", "Emma", "Francis", "George",
         "Harold", "Imogen", "Jackie", "Kurt", "Linda"]
print(names[3:5])
print(names[1:6])
print(names[5:12])
print(names[5:])
print(names[11])
print(names[-1])
print(names[1:8:2])
print(names[0:11:2])
print(names[0::2])
print(names[11:8:-1])
print(names[11::-1])
print(names[::-1])

# problem 2 creates a function that takes a list as a parameter and returns as true if there
# is more than one of the same item on the list


def are_duplicates(nums):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] == nums[y]:
                return True
    return False


print(are_duplicates([100, 2, 3, 4, 100]))

# problem 3


def add_numbers(nums):
    total = 0
    for x in nums:
        total += x
    return total


print(add_numbers([9, 5, 11, 6, 1, 15]))

# problem 4


def has22(nums):
    for x in range(len(nums)-1):
        if nums[x] == 2 and nums[x + 1] == 2:
            return True
    return False


print(has22([1, 2, 3, 4, 5, 2, 2]))

# problem 5


def is_sorted(nums):
    while True:
        for x in range(1, len(nums)):
            if nums[x - 1] > nums[x]:
                return False
        return True


print(is_sorted(["b", "a"]))

# problem 6


def remove_duplicates(nums):
    removed = []
    for x in nums:
        if x not in removed:
            removed.append(x)
    return removed


print(remove_duplicates([2, 2, 3, 4, 9, 9]))

# problem 7


def get_max(nums):
    biggest_num = nums[0]
    for x in nums:
        if x > biggest_num:
            biggest_num = x
    return biggest_num


print(get_max([-6, -9, 48, -89]))

# problem 8


def get_min(nums):
    smallest_num = nums[0]
    for x in nums:
        if x < smallest_num:
            smallest_num = x
    return smallest_num


print(get_min([-6, -4443, 48, -86]))
