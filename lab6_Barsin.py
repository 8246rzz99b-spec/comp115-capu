"""
Exercise 1
"""
def is_in_list(nums, k):
    for num in nums:
        if num == k:
            return True
    return False


assert is_in_list([4, 5, 6], 5) == True
assert is_in_list([], 3) == False
assert is_in_list([-3, -2, -1, 0], -1) == True



"""
Exercise 2
"""
def has_negative(nums):
    for num in nums:
        if num < 0:
            return True
    return False


assert has_negative([1, 2, 3, -4, 5]) == True
assert has_negative([0, 2, 3, 4, 5]) == False



"""
Exercise 3
"""
def all_even(nums):
    for num in nums:
        if num % 2 != 0:
            return False
    return True


assert all_even([2, 4, 6, 8]) == True
assert all_even([2, 3, 4]) == False



"""
Exercise 4
"""
def count_even_odd(nums):
    even_count = 0
    odd_count = 0

    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return [even_count, odd_count]


assert count_even_odd([1, 2, 3, 4, 5, 6]) == [3, 3]
assert count_even_odd([2, 4, 6, 8]) == [4, 0]
assert count_even_odd([1, 3, 5]) == [0, 3]



"""
Exercise 5
"""
def temp_category(temps):
    hot = 0
    mild = 0
    cold = 0

    for t in temps:
        if t >= 30:
            hot += 1
        elif 15 <= t <= 29:
            mild += 1
        else:
            cold += 1

    return [hot, mild, cold]


assert temp_category([32, 28, 15, 12, 35]) == [2, 2, 1]
assert temp_category([10, 5, 0]) == [0, 0, 3]
assert temp_category([20, 25, 30]) == [1, 2, 0]



"""
Exercise 6
"""
def mult_category(nums):
    result = []

    for num in nums:
        if num % 2 == 0:
            result.append(2)
        elif num % 3 == 0:
            result.append(3)
        elif num % 5 == 0:
            result.append(5)
        else:
            result.append("O")

    return result


assert mult_category([2, 3, 5, 7]) == [2, 3, 5, "O"]
assert mult_category([4, 9, 10, 11]) == [2, 3, 2, "O"]
assert mult_category([15, 7, 30, 11]) == [3, "O", 2, "O"]



"""
Exercise 7
"""
def reverse_list(nums):
    reversed_nums = []

    for i in range(len(nums) - 1, -1, -1):
        reversed_nums.append(nums[i])

    return reversed_nums


assert reverse_list([1, 3, 4]) == [4, 3, 1]
assert reverse_list([3, 9, 6]) == [6, 9, 3]



"""
Exercise 8
"""
def remove_duplicates(nums):
    new_list = []

    for num in nums:
        if num not in new_list:
            new_list.append(num)

    return new_list


assert remove_duplicates([1, 3, 3, 4]) == [1, 3, 4]
assert remove_duplicates([1, 1, 3, 4, 3]) == [1, 3, 4]



"""
Exercise 9
"""
def my_factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


assert my_factorial(0) == 1
assert my_factorial(1) == 1
assert my_factorial(3) == 6
assert my_factorial(5) == 120



"""
Exercise 10
"""
def my_fib(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    fib = [0, 1]

    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])

    return fib


assert my_fib(1) == [0]
assert my_fib(2) == [0, 1]
assert my_fib(5) == [0, 1, 1, 2, 3]
assert my_fib(7) == [0, 1, 1, 2, 3, 5, 8]


