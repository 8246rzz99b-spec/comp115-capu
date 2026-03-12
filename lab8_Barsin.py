import re

# Exercise 1
def remove_duplicates_set(s):
    """
    Remove duplicate characters from a string using a set.
    The order of characters stays the same.
    """
    result = ""
    seen = set()

    for char in s:
        if char not in seen:
            seen.add(char)
            result += char

    return result


# Unit tests
assert remove_duplicates_set("apple") == "aple"
assert remove_duplicates_set("Popsipple") == "Popsile"
assert remove_duplicates_set("pear") == "pear"


# Exercise 2
def gem_counting(stones, gems):
    """
    Count how many stones are gems.
    stones = stones collected
    gems = gem types
    """
    gem_set = set(gems)
    total = 0

    for stone in stones:
        if stone in gem_set:
            total += 1

    return total


# Unit tests
assert gem_counting("abDFMdm", "admMQq") == 4
assert gem_counting("abDFMdm", "af") == 1
assert gem_counting("awCcM", "cQqW") == 1
assert gem_counting("bFfL", "cQqW") == 0


# Exercise 3
def students_id(ids):
    """
    Return the number of different student ids in the list.
    """
    return len(set(ids))


# Unit tests
assert students_id(['002', '003', '001', '004', '012']) == 5
assert students_id(['002', '003', '001', '012', '003', '001']) == 4


# Exercise 4
def students_id_occurrences(ids):
    """
    Count how many times each student id appears.
    """
    counts = {}

    for student in ids:
        if student in counts:
            counts[student] += 1
        else:
            counts[student] = 1

    return counts


# Unit tests
assert students_id_occurrences(['002', '003', '001', '004', '012']) == {
    '002': 1, '003': 1, '001': 1, '004': 1, '012': 1
}

assert students_id_occurrences(['002', '003', '001', '012', '003', '001']) == {
    '002': 1, '003': 2, '001': 2, '012': 1
}


# Exercise 5
def word_frequency(paragraph):
    """
    Count how many times each word appears in a paragraph.
    Returns a dictionary where the key is the word and the value is the count.
    """
    words = re.findall(r'\b\w+\b', paragraph)
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


# Unit tests
assert word_frequency("I am alive. I am happy.") == {
    'I': 2, 'am': 2, 'alive': 1, 'happy': 1
}

assert word_frequency("I do not like water. I like fruits.") == {
    'I': 2, 'do': 1, 'not': 1, 'like': 2, 'water': 1, 'fruits': 1
}