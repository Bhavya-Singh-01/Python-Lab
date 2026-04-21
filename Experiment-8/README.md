Experiment: Regular Expressions in Python

AIM:
To implement the use of Regular Expressions (`re` module) in Python for pattern matching, searching, finding, substitution, splitting, and validation.

ALGORITHM:
1. Import the `re` module.  
2. Define a text string containing a phone number and email.  
3. Use `re.match()` to check if the string starts with a given pattern.  
4. Use `re.search()` to find a phone number in the string.  
5. Use `re.findall()` to extract all digits from the string.  
6. Use `re.finditer()` to find digits along with their positions.  
7. Use `re.sub()` to replace digits with `*`.  
8. Use `re.split()` to split the string based on spaces.  
9. Take date input from the user.  
10. Define a pattern for date format (`dd/mm/yyyy`).  
11. Use `re.fullmatch()` to validate the date format.  
12. Display whether the date is valid or invalid.
