# ==============================
# Exercise 1
# ==============================

def reverse_str(s):
    """
    Reverse a string.

    Parameters:
    s (str): input string

    Returns:
    str: reversed string
    """
    result = ""
    for ch in s:
        result = ch + result
    return result


assert reverse_str("Abd") == "dbA"
assert reverse_str("COMP115") == "511PMOC"
assert reverse_str("") == ""
assert reverse_str("a") == "a"



# ==============================
# Exercise 2
# ==============================

def count_vowels(s):
    """
    Count the number of vowels in a string.

    Parameters:
    s (str): input string

    Returns:
    int: number of vowels
    """
    s = s.lower()
    count = 0

    for ch in s:
        if ch in "aeiou":
            count += 1

    return count


assert count_vowels("Apple") == 2
assert count_vowels("Hmmm") == 0
assert count_vowels("AEIOU") == 5
assert count_vowels("") == 0



# ==============================
# Exercise 3
# ==============================

def remove_duplicates(s):
    """
    Remove duplicate characters from a string.

    Parameters:
    s (str): input string

    Returns:
    str: string with duplicate characters removed
    """
    result = ""

    for ch in s:
        if ch not in result:
            result += ch

    return result


assert remove_duplicates("apple") == "aple"
assert remove_duplicates("Popsipple") == "Popsile"
assert remove_duplicates("pear") == "pear"
assert remove_duplicates("aaaa") == "a"



# ==============================
# Exercise 4
# ==============================

def find_index(s, t):
    """
    Find the lowest index of character t in string s.

    Parameters:
    s (str): string to search
    t (str): character to find

    Returns:
    int: index of t in s, or -1 if not found
    """
    for i in range(len(s)):
        if s[i] == t:
            return i

    return -1


assert find_index("Abd", "b") == 1
assert find_index("Abdccc", "c") == 3
assert find_index("Abd", "w") == -1
assert find_index("hello", "h") == 0



# ==============================
# Exercise 5
# ==============================

days_week = (
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
)

def project_completion_day(day, days_to_completion):
    """
    Calculate the project completion day.

    Parameters:
    day (str): current day
    days_to_completion (int): number of days needed

    Returns:
    str: completion day
    """

    start_index = days_week.index(day)
    finish_index = (start_index + days_to_completion) % 7

    return days_week[finish_index]


assert project_completion_day("Monday", 4) == "Friday"
assert project_completion_day("Monday", 7) == "Monday"
assert project_completion_day("Saturday", 2) == "Monday"
assert project_completion_day("Saturday", 1) == "Sunday"



# ==============================
# Exercise 6 - Log Parsing
# ==============================

def parse_log_line(line):
    """
    Parse a log line into components.

    Parameters:
    line (str): log line

    Returns:
    tuple: (timestamp, level, module, message)
    """

    parts = line.split()

    timestamp = parts[0] + " " + parts[1]
    level = parts[2][1:-1]
    module = parts[3]
    message = " ".join(parts[4:])

    return (timestamp, level, module, message)


line = "2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s"

assert parse_log_line(line) == (
    "2024-03-05 14:32:15",
    "ERROR",
    "database.py",
    "Connection timeout after 30s"
)



# Parse all logs

log_string = """
2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s
2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)
2024-03-05 14:32:22 [INFO] server.py Server started on port 8000
2024-03-05 14:32:45 [ERROR] database.py Connection lost to primary
2024-03-05 14:33:02 [WARNING] cache.py Redis connection unstable
2024-03-05 14:33:15 [ERROR] api.py Request handler crashed
2024-03-05 14:33:22 [INFO] database.py Attempting reconnect
"""

parsed_logs = []

lines = log_string.strip().split("\n")

for line in lines:
    parsed_logs.append(parse_log_line(line))


print(parsed_logs)