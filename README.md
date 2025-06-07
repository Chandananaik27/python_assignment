# python_assignment
# **1. `calendar_module()`**

- This Python script defines a function `calendar_module()` to determine the day of the week for a given input date.
- It prompts the user to input a date in the format 'MM-DD-YEAR', converts it to a `datetime.date` object, calculates the day of the week using `.weekday()`, and returns the corresponding day in uppercase after logging it.
# ****2. collections_namedtuples()****

* This Python script defines a function calculate_average() to compute the average marks of students. 
* It first reads the number of students, their column names, and calculates the average of marks by summing up marks and dividing by the number of students. 
* The script then logs the result to two decimal places using the logging module.
# **3. `read_student_marks()`**
- This Python script defines a function read_student_marks() to read student names and their marks.
- It prompts the user to input the number of students, their names, and marks. Then, it computes the average marks for a queried -student's name by extracting their marks from the dictionary.
# **4. `floor_ceil_rint()`**

- This Python script defines a function `floor_ceil_rint()` to perform floor, ceil, and round operations on an input array using NumPy.
- It reads a space-separated input and converts it into a NumPy array of floats. Then, it calculates the floor, ceil, and rounded values of the array elements.

# **5. `iterator()`**

- This Python script defines a function `iterator()` to calculate the probability of selecting at least one unique letter from a given list of letters for a specific number of selections.
- It reads an integer n, a list of letters, and another integer k. Then, it computes the total number of combinations and the combinations that include at least one unique letter among the first k selections.

# **6. `linear_algebra()`**

- This Python script defines a function `linear_algebra()` to compute the determinant of a square matrix.
- It reads an integer n representing the size of the square matrix and then reads the matrix itself row by row. It utilizes NumPy's `np.linalg.det()` function to compute the determinant of the matrix.

# **7. `is_valid_email()`**

- This Python script defines a function `is_valid_email()` to filter and validate a list of email addresses based on a specific regex pattern.
- It reads an integer n representing the number of email addresses and then reads n email addresses into a list. It filters them using the `is_valid_email()` function based on whether they match the defined email format.

# **8. `calculate_statistics()`**

- This Python script defines a function `calculate_statistics()` to compute statistics (mean, variance, and standard deviation) along rows for a 2D array.
- It reads two integers representing the dimensions of the array and then reads the array row by row. Using NumPy functions, it computes the mean, variance, and standard deviation along the rows respectively.

# **9. `merge_tools()`**

- This Python script defines a function `merge_tools()` to split a string into substrings of a specified length, removing duplicate characters within each substring.
- It reads the input string and the integer k. Then, it iterates over the string in steps of k, creating substrings. Within each substring, it keeps track of unique characters and appends them to the result list.

# **10. `min_max()`**

- This Python script defines a function `min_max()` to find the maximum value among the minimum values of each row in a 2D array.
- It reads an integer X representing the number of rows and then reads the array row by row. Utilizing NumPy's `np.min()` function with axis=1, it computes the minimum values along the rows, then finds the maximum of these minimum values.

# **11. `mutate_string()`**

- This Python script defines a function `mutate_string()` to replace a character in a string at a specified position.
- It reads an input string and a position-character pair. Then, it replaces the character at that position in the string with the specified character.

# **12. `calculate_happiness()`**

- This Python script defines a function `calculate_happiness()` to compute happiness based on elements in an array that are liked or disliked.
- It reads two integers n and m representing the size of the array and the number of elements in the like and dislike sets respectively.

# **13. `can_stack_cubes()`**

- This Python script defines a function `can_stack_cubes()` to determine if a given arrangement of cubes can be stacked.
- It reads an integer T representing the number of test cases. For each test case, it reads an integer n indicating the number of cubes and a list of integers representing the sizes of the cubes.

# **14. `second_maximum()`**

- This Python script defines a function `second_maximum()` to find the second maximum value among a list of values.
- It prompts the user to input the number of values and the values themselves. Then, it sorts the values in ascending order and returns the second largest value.

# **15. `string_formatting()`**

- This Python script defines a function `string_formatting()` to print formatted representations of numbers up to a specified maximum value.
- It reads an integer number representing the maximum value to print and then calculates decimal, octal, hexadecimal, and binary representations for each number from 1 to the maximum value.

# **16. `text_alignment()`**

- This Python script defines a function `text_alignment()` to print the HackerRank logo using a specified character and thickness.
- It reads an integer thickness representing the thickness of the logo and then iterates through different sections of the logo, printing each section accordingly.

# **17. `time_delta()`**

- This Python script defines a function `time_delta()` to compute the absolute time difference in seconds between two timestamps provided in a specific format.
- It reads the number of test cases and then iterates through each test case. For each test case, it reads two timestamps as strings and converts them into datetime objects using a specified date format.

# **18. `word_order()`**

- This Python script defines a function `word_order()` to count the occurrences of words in a list and determine the number of distinct words.
- It reads an integer n representing the number of words, followed by n words into a list. Then, it iterates through the list, counting the occurrences of each word using a dictionary.
