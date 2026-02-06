#-------------------------------------------------------------------------------------------------
#Exercise 1
def  convert_american_dollars(american_dollars):
  canadian_dollars = american_dollars * 1.34    #needed calculation to get the canadian equivalent
  return round(canadian_dollars, 2) #rounding up by 2 decimel points


american_dollars = float(input("How much money do you want to convert to CAD?"))

canadian_dollars = convert_american_dollars(american_dollars)

print(f"You have {canadian_dollars} CAD")

assert convert_american_dollars(1) == 1.34
assert convert_american_dollars(100) == 134
assert convert_american_dollars(100.05) == 134.07
#-------------------------------------------------------------------------------------------------
#Exercise 2
def back_day_from_trip(day_today, days_trip):
    day_return = (day_today + days_trip) % 7
    days_week = ["Monday", "Tuesday", "Wednesday",
                 "Thursday", "Friday", "Saturday", "Sunday"]
    return days_week[day_return]

print(back_day_from_trip(3, 5))
print(back_day_from_trip(1, 2))
print(back_day_from_trip(1, 7))

assert back_day_from_trip(3, 5) == "Tuesday"
assert back_day_from_trip(1, 2) == "Thursday"
assert back_day_from_trip(1, 7) == "Tuesday"
#-------------------------------------------------------------------------------------------------
#Exercise 3
def average(nums):
   total = 0
   for num in nums:
      total += num   #add each number manually

   average = total / len(nums)
   return round(average, 2)  #used len to get how many numbers are there
   
print(average([1, 2, 3]))
print(average([1, 2, 3, 4]))
print(average([2, 9, 2]))

assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 4]) == 2.5
assert average([2, 9, 2]) == 4.33
#-------------------------------------------------------------------------------------------------
#Exercise 4
def sum_of_squares(numbers):
   total = 0
   for n in numbers:
      total += n ** 2
   return total

print(sum_of_squares([2, 3, 4]))
print(sum_of_squares([2, 4]))
print(sum_of_squares([]))

assert sum_of_squares([2, 3, 4]) == 29
assert sum_of_squares([2, 4]) == 20
assert sum_of_squares([]) == 0
#-------------------------------------------------------------------------------------------------
#Exercise 5
def add_number(nums2, k):
    result = []
    for n in nums2:
        result.append(n + k)
    return result

print(add_number([2, 4, 1], 5))
print(add_number([7, 8], -5))

assert add_number([2, 4, 1], 5) == [7, 9, 6]
assert add_number([7, 8], -5) == [2, 3]
#-------------------------------------------------------------------------------------------------
#Exercise 6
def squares(nums3):
    result = []
    for n in nums3:
        result.append(n ** 2)    #add squared number into list
    return result

print(squares([2, 3, 4]))
print(squares([2 ,4]))
print(squares([5, 6, 7]))
print(squares([]))

assert squares([2, 3, 4]) == [4, 9, 16]
assert squares([2, 4]) == [4, 16]
assert squares([5, 6, 7]) == [25, 36, 49]
assert squares([]) == []
   #-------------------------------------------------------------------------------------------------
#Exercise 7
def repeat_elements(nums4):
    result = []
    for n in nums4:
        result.append(n)   # add number first time
        result.append(n)   # add number second time
    return result

print(repeat_elements([1, 2, 3, 4]))
print(repeat_elements([2, 7, 8]))
print(repeat_elements([]))

assert repeat_elements([1, 2, 3, 4]) == [1, 1, 2, 2, 3, 3, 4, 4]
assert repeat_elements([2, 7, 8]) == [2, 2, 7, 7, 8, 8]
assert repeat_elements([]) == []
