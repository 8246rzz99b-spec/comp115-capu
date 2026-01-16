# Exercise 1 (10 marks)
num = 5
new_num = num * (10 - 5)
print(f"Exercise 1: new_num stores the value of {new_num}")
# The reason the answer was 45 at first it is because multiplication would be  the first that would happen in a equation.
#-----------------------------------------------------------------------------------------------------------------------
print("")
# Exercise 2 (10 marks)

dividend = 10
divisor = 3

division_result = dividend / divisor

quotient = dividend // divisor   # The quotiont should be 3
remainder = dividend % divisor  # The remainder should be 1

print(f"""Exercise 2: 
{dividend} / {divisor} = {division_result} (decimal result)
{dividend} / {divisor} = {quotient} remainder {remainder}""")
# I changed the divison to integer division for line 15 and I used modulus operator for line 16.
#-----------------------------------------------------------------------------------------------------------------------
print("")
# Exercise 3 (20 marks)

marks = [80.5, 85.3, 76.5, 79.7]    # A list of a student's first-term course marks
marks_average = (marks[0] + marks[1] + marks[2] + marks[3]) / 4   #Correct to get the average of all marks 80.5
print(f"Exercise 3: The average mark is {marks_average}")
# To get the average we need to add all marks together and divid it by the number of marks
#-----------------------------------------------------------------------------------------------------------------------
print("")
#Exercise 4 (20 marks)

radius = 2
area = 3.14 * radius * radius
print(f"Exercise 4: The area of a circle with radius 2 is {area}")
# Done
#-----------------------------------------------------------------------------------------------------------------------
print("")
#Exercise 5 (30 marks)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] # To have the days on the message that is printing
print("Exercise 5:")

day_today = int(input("Enter today's day number (0=Monday, 1=Tuesday, 2=Wednesday, 3=Thursday, 4=Friday, 5=Saturday, 6=Sunday): ")) 
# show the numbers that the person that is typing know what number to put and used "int" to change the answer from string to integ

days_trip = int(input("Enter the number of days for your trip: "))

day_return = (day_today + days_trip) % 7 # calculate the day that the person is returning by using the modulus operator "%"

# And at the end print the result using an f-string
print(f"Your trip starts on day {day_today} ({days[day_today]}), lasts {days_trip} days. You are back on day {day_return} ({days[day_return]}).")
#-----------------------------------------------------------------------------------------------------------------------

