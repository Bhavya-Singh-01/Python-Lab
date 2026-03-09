# Experiment 1
## Demonstrate Various Data Types and Operators in Python

### Aim
To demonstrate various data types and operators in Python.

### Algorithm
1. Start the program.
2. Declare variables of different data types such as integer, float, string, and boolean.
3. Display the values of the variables.
4. Perform arithmetic operations like addition, subtraction, multiplication, and division.
5. Perform comparison operations such as greater than, less than, and equal to.
6. Perform logical operations like AND, OR, and NOT.
7. Display the results.
8. Stop the program.

Source Code
a=315
b=800
print("\nEquation Assignment Operators:\n")

print((a + b)**2 == a**2 + 2 * (a * b) + b**2)
print((a - b)**2 == a**2 - 2 * (a * b) + b**2)
print((a + b) * (a + b) == 2 * (a**2 - b**2))
print((a + b) + (a - b) == a**2 - b**2)
print(a**3 + b**3 == (a + b) * (a**2 - a * b + b**2))


print("\nBitwise Operators:\n")
print(a // b == (a ^ b) + (a & b))
print(a ^ (a & b) == (a // b) ^ b)
print(b ^ (a & b) == (a // b) ^ a)
print((a & b) ^ (a // b) == a ^ b)


print("\nAddition:\n")
print((a + b) == (a ^ b) + (a & b))
print(a + b == (a ^ b) + 2 * (a & b))


print("\nSubtraction:\n")
print(a - b == (a ^ (a & b)) - ((a // b) ^ a))
print(a - b == ((a // b) ^ b) - ((a // b) ^ a))
print(a - b == (a ^ (a & b)) - (b ^ (a & b)))
print(a - b == ((a // b) ^ b) - (b ^ (a & b)))

Output:
Equation Assignment Operators:

True
True
False
False
True

Bitwise Operators:

False
False
False
False

Addition:

False
True

Subtraction:

False
False
True
False
